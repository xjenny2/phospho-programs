import csv
with open("/Users/jennyxu/Desktop/phospho-files/results_no_zeroes.txt", 'r') as f, open("/Users/jennyxu/Desktop/phospho-files/phospho_muc16.txt", 'w') as r, open("/Users/jennyxu/Desktop/phospho-files/muc16.txt", 'r') as n:
    r.write("origin\taf\tisSite\n")
    reader = csv.DictReader(f, delimiter = "\t")
    results = []
    for row in reader:
        substrate = row["substrate"]
        kinase = row["kinase"]
        pos = row["position"]
        af = float(row["alleleFrequency"])
        isSite = row["isSite"]
        hasRepeat = False
        if substrate == "MUC16":
            for result in results:
                if (result[0] == pos and result[1] == af):
                    hasRepeat = True
            if not hasRepeat:
                results.append([pos, af])
                r.write("phospho" + "\t" + str(af) + '\t' + isSite + '\n')
                print("ok")
            else:
                print(str(af) + '\t' + isSite)
        else:
            print("nope")
    otherReader = csv.DictReader(n, delimiter = "\t")
    for otherRow in otherReader:
        othersubstrate = otherRow["substrate"]
        otherpos = otherRow["position"]
        otheraf = float(otherRow["alleleFrequency"])
        if otheraf != 0:
            r.write("regular" + '\t' + str(otheraf) + '\tFalse\n')









