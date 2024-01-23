fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print("File not found.")
    quit()

if len(fname) < 1:
    fname = "mbox-short.txt"

count = 0

for line in fh:
    
    if not line.startswith('From:'):
        continue
    count = count + 1
    lines = line.split()
    print(lines[1])

print("There were", count, "lines in the file with From as the first word")