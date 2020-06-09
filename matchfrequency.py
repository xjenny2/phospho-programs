import re
import gnomad
import ensembl
import csv
import sys
import time
def find_freq(protein_name, motif_list):



    # Opens sequence file and finds amino acid location of any matches to the motif
    canonical_id = gnomad.get_canonical_id(protein_name)
    tries = 0
    while canonical_id == "error":
        print("Error, retrying")
        time.sleep(1)
        canonical_id = gnomad.get_canonical_id(protein_name)
        if tries > 10:
            print("Gnomad Canonical ID connection error")
            sys.exit()
        tries += 1

    matches = []
    sequence = ensembl.get_sequence(canonical_id)
    triesSeq = 0
    while sequence == "error":
        print("Error, retrying")
        time.sleep(1)
        sequence = ensembl.get_sequence(canonical_id)
        if triesSeq > 10:
            print("Ensembl Connection error")
            sys.exit()
        triesSeq += 1
    sequence = sequence.replace("\n", "")
    for motif in motif_list:
        name = motif[0]
        fullMotif = motif[1]
        site = motif[2]
        for match in re.finditer(fullMotif, sequence):
            for aaIndex in range(0, len(match.group())):
                isSite = False
                for phosphoAA in re.finditer(site, match.group()):
                    if (aaIndex == phosphoAA.start()):
                        isSite = True
                matches.append([name, match.start() + aaIndex + 1, match.group()[aaIndex], isSite])

    print("Matches found")

    mutations = gnomad.get_variants(canonical_id)
    triesMut = 0
    while mutations == "error":
        print("Error, retrying")
        time.sleep(1)
        mutations = gnomad.get_variants(canonical_id)
        if triesMut > 10:
            print("Gnomad Mutations Connection error")
            sys.exit()
        triesMut += 1

    results = []  # final results
    for match in matches:
        matchPattern = re.compile(r'(?<=p.[A-Z][a-z]{2})' + str(match[1]) + '(?=[A-Z][a-z]+)')  # AA change/place
        hasMatch = False
        for mutation in mutations:
            consequence = mutation.get('consequence')
            af = mutation.get('af')
            m = matchPattern.search(consequence)
            if m:
                results.append([protein_name, match[0], match[1], af, match[3]])  # [location, frequency]
                hasMatch = True
        if not hasMatch:
            results.append([protein_name, match[0], match[1], 0, match[3]])  # appends 0 for frequency if there is no match
    print("Results found")
    return(results)


if __name__ == '__main__':
    name = input("Enter the name of the protein: ")
    with open('/Users/jennyxu/Desktop/phospho-files/motifs_test.txt') as p:
        patternList = list(csv.reader(p, delimiter='\t'))
        print(find_freq(name, patternList))
