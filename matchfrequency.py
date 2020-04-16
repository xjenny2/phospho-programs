import re
import gnomad
import ensembl

def find_freq(protein_name, patternlist):



    # Opens sequence file and finds amino acid location of any matches to the motif
    canonical_id = gnomad.get_canonical_id(protein_name)

    matches = []
    seq = ensembl.get_sequence(canonical_id)
    for l in patternlist:
        name = l[0]
        pattern = l[1]
        site = l[2]
        for match in re.finditer(pattern, seq):
            # for x in range(match.start(), match.end()):
            #     isSite = False
            #     if (site_atm.search(match.group()).start() + match.start() == x):
            #         isSite = True
            #     matches.append([x + 1, match.group()[x-match.start()], isSite])
            for x in range(0, len(match.group())):
                isSite = False
                if (re.search(site, match.group()).start() == x):
                    isSite = True
                matches.append([name, match.start() + x + 1, match.group()[x], isSite])

    print("\nMatches found: ")
    print(matches)

    mutations = gnomad.get_variants(canonical_id)

    results = []  # final results
    for match in matches:
        match_pattern = re.compile(r'(?<=p.[A-Z][a-z]{2})' + str(match[1]) + '(?=[A-Z][a-z]+)')  # AA change/place
        has_match = False
        for mutation in mutations:
            consequence = mutation.get('consequence')
            af = mutation.get('af')
            m = match_pattern.search(consequence)
            if m:
                results.append([match[0], match[1], af, match[3]])  # [location, frequency]
                has_match = True
        if not has_match:
            results.append([match[0], match[1], 0, match[3]])  # appends 0 for frequency if there is no match
    print("Results found")
    return(results)


if __name__ == '__main__':
    name = input("Enter the name of the protein: ")
    patternList = [["ATM", "SQ", "S(?=Q)"], ["DNAPK", "P[ST][A-Z]", "(?<=P)[ST](?=[A-Z])"]]
    print(find_freq(name, patternList))
