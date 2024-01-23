fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
handle = open(fname)

dic = dict()

for line in handle:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        # idiom : retrieve/create/update counter
        dic[w] = dic.get(w, 0) + 1

x = sorted(dic.items())
# print(x[:5])

tmp = list()
for k,v in dic.items():
    # print(k,v)
    newt = (v,k)
    tmp.append(newt)

# print('Fliped', tmp)

tmp = sorted(tmp, reverse=True)
# print('Sorted', tmp[:5])

for v, k in tmp[:5]:
    print(k,v)