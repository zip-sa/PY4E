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
            email = words[1]
            counts_dic[email] = counts_dic.get(email, 0) + 1

x = sorted(counts_dic.items())

tmp = list()
for k, v in counts_dic.items():
    newt = (v, k)
    tmp.append(newt)

tmp = sorted(tmp, reverse=True)

for v, k in tmp[:1]:
    print(k, v)