try:
    hrs = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except:
    print('Error, please enter numeric input')
    exit()

if hrs > 40:
    over_hrs = hrs - 40
    total_wage = (40 * rate) + (over_hrs * rate * 1.5)
    print(total_wage)
else:
    total_wage = hrs * rate
    print(total_wage)