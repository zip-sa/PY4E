fname = "mbox-short.txt" #input("Enter file name: ")

try:
    fh = open(fname)
except:
    print("File not found.")
    quit()

#if len(fname) < 1:
#    fname = "mbox-short.txt"

counts = dict()

for line in fh:
    if not line.startswith('From:'):
        continue
    print('Print lines :', line)
    words = line.split()
    print('Print words : ', words)
    days = words[1]
    for day in days:
        counts[day] = counts.get(day,0)+1

print(counts)