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
        
# print(dic)

# now we want to fine the most common word 
largest = -1
theword = None

for k, v in dic.items():
     print(k,v)
     if v > largest :
        largest = v
        theword = k #cature/remember the word that was largest
        
print('Done', theword, largest)