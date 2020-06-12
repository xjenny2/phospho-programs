import re
import gnomad
import ensembl
import csv
import sys
import time
def find_norm_freq(protein_name):



    # Opens sequence file and finds amino acid location of any matches to the motif
    canonical_id = gnomad.get_canonical_id(protein_name)


    mutations = gnomad.get_variants(canonical_id)

    results = []  # final results
    for mutation in mutations:
        matchPattern = re.compile(r'(?<=p\.[A-Z][a-z][a-z])\d+(?=[A-Z][a-z]{2}$)')  # AA change/place
        consequence = mutation.get('consequence')
        af = mutation.get('af')
        m = matchPattern.search(consequence)
        if m:
            results.append([protein_name, consequence, af])  # [location, frequency]
    print("Results found")
    return(results)


results = find_norm_freq("OBSCN")
with open("/Users/jennyxu/Desktop/phospho-files/obscn.txt", 'w') as f:
    for result in results:
        for item in result:
            f.write(str(item))
            f.write("\t")
        f.write("\n")
#
