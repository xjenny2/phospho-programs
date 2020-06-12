import csv
with open("/Users/jennyxu/Desktop/phospho-files/results.txt", 'r') as f, open("/Users/jennyxu/Desktop/phospho-files/results_no_zeroes.txt", 'w') as r:
    reader = csv.DictReader(f, delimiter = "\t")
    for row in reader:
        substrate = row["substrate"]
        kinase = row["kinase"]
        pos = row["position"]
        af = float(row["alleleFrequency"])
        isSite = row["isSite"]
        print(af)
        if af != 0:
            r.write(substrate + "\t" + kinase + "\t" + str(pos) + "\t" + str(af) + "\t" + isSite + "\n" )




