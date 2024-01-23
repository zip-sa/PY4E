# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

confidence_total = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    ipos = line.find(':')
    confidence_total = float(confidence_total) + float(line[ipos+2:])
    count = count + 1
    # print(line)

confidence_avg = confidence_total / count
print("Average spam confidence:", confidence_avg)
# print("Done")
