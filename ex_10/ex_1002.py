try:
    fname = input('Enter File: ')
    if len(fname) < 1 : fname = 'mbox-short.txt'

except:
    print('That file name is not exsisting')
    quit()

handle = open(fname)

counts_dic = dict()

for line in handle:
    if line.startswith('From '):
        words = line.split()
        if len(words) > 2:
            time = words[5].split(':')
            hour = time[0]
            counts_dic[hour] = counts_dic.get(hour, 0) + 1

tmp = list()
for k, v in counts_dic.items():
    newt = (k, v)
    tmp.append(newt)


for k, v in sorted(tmp[:]):
    print(k, v)