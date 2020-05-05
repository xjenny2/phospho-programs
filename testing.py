import matchfrequency
import time
from itertools import islice
import csv

with open('/Users/jennyxu/Desktop/phospho-files/genes_edited.txt', 'r') as f, open('/Users/jennyxu/Desktop/phospho-files/results.txt', 'w') as r, open('/Users/jennyxu/Desktop/phospho-files/motifs_test.txt') as p:
   patternList = list(csv.reader(p, delimiter='\t'))
   count = 0
   while count < 30:
       for line in islice(f, 0, 10):
            print(line.strip() + ":")
            # for result in matchfrequency.find_freq(line.strip(), patternList):
            #     for item in result:
            #         r.write(str(item))
            #         r.write("\t")
            #     r.write("\n")
            # print("Written to file\n\n")
       count = count + 2
       print ("Waiting")
       time.sleep(10)
