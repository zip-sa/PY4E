largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        num = int(num)
    except:
        print('Invalid input')
        continue
    

    if largest is None or largest < num : largest = num
    # print(largest)
    if smallest is None or smallest > num : smallest = num
    # print(smallest)

    # print(num)

print("Maximum is", largest)
print("Minimum is", smallest)