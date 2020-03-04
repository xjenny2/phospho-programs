import matchfrequency

# Opening file
f = open('/Users/jennyxu/Desktop/phospho-files/genes.txt', 'r')
count = 0
# Using for loop
while count < 20:
    for line in f:
        count += 1
        print(line.strip())
        matchfrequency.find_freq(line.strip())