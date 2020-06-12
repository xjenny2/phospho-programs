import csv
import gnomad
import ensembl
from collections import Counter

with open("/Users/jennyxu/Desktop/phospho-files/results_no_zeroes.txt", 'r') as f, open("/Users/jennyxu/Desktop/phospho-files/test.txt", 'w') as r:
    reader = csv.DictReader(f, delimiter="\t")
    results = []
    for row in reader:

        results.append(row["substrate"])
    for result, number in Counter(results).most_common(30):
        seq = ensembl.get_sequence(gnomad.get_canonical_id(result))
        seq = seq.replace("\n", "")
        print(seq)
        r.write(result + "\t" + str(len(seq)) + "\t" + str(number) + "\n")




