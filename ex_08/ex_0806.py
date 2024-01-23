mlist = []

while True:
    try:
        num = input("Enter the number: ")
        if num == 'done':
            break
        fnum = float(num)
    except:
        print('Invalid input')
        continue

    mlist.append(fnum)

print("Maximum:", max(mlist))
print("Minimum:", min(mlist))
#print(mlist)
