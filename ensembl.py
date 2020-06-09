import requests
import sys


def get_sequence(canonical_id):

    server = "http://grch37.rest.ensembl.org"
    ext = "/sequence/id/" + canonical_id + "?format=fasta;type=protein"
    r = requests.get(server + ext, headers={"Content-Type": "text/x-fasta"})

    if not r.ok:
        r.raise_for_status()
        return "error"
    seqlist = r.text.split("\n", 1)

    sequence = seqlist[1]

    print("Sequence found")
    return sequence
