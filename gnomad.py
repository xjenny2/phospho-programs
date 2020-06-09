import requests


def get_canonical_id(gene_name):
    query = """
    {
        gene(gene_name: "%s") {
        canonical_transcript_id
        }     
    }""" % gene_name
    res = requests.post('https://gnomad.broadinstitute.org/api', json={'query': query})
    if res.ok:
        print("Canonical ID retrieved:" + res.json()['data']['gene']['canonical_transcript_id'])
        return res.json()['data']['gene']['canonical_transcript_id']
    else:
        res.raise_for_status()
        return "error"


def get_variants(transcript_id):
    print("Searching for variants...")
    query = """
    {
        transcript(transcript_id: "%s") {
            variants(dataset: gnomad_r2_1) {
                hgvsp
                exome {
                    ac
                    an
                }
                genome {
                    ac
                    an
                }
            }
        }
    }""" % transcript_id
    res = requests.post('http://gnomad.broadinstitute.org/api', json={'query': query})
    if res.ok:
        print("Variants found--processing data")
        variants = res.json()['data']['transcript']['variants']
        results = []
        for variant in variants:
            consequence = variant.get('hgvsp')
            exome_info = variant.get('exome')
            genome_info = variant.get('genome')
            result = {}
            if consequence is not None and (exome_info is not None or genome_info is not None):
                result['consequence'] = consequence
                if exome_info is not None:
                    ac_exome = exome_info.get('ac')
                    an_exome = exome_info.get('an')
                else:
                    ac_exome = 0
                    an_exome = 0
                if genome_info is not None:
                    ac_genome = genome_info.get('ac')
                    an_genome = genome_info.get('an')
                else:
                    ac_genome = 0
                    an_genome = 0
                if an_exome == 0 and an_genome == 0:
                    result ['af'] = 0
                    print("Error: exome/genome values at " + consequence)
                else:
                    result['af'] = (ac_exome + ac_genome) / (an_exome + an_genome)
                results.append(result)
        return results
    else:
        res.raise_for_status()
        return "error"
