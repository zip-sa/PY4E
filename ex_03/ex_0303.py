score = input("Enter Score: ")

try:
    fscore = float(score)
except:
    print('Error, please enter numeric input')
    exit()

if fscore >= 0.9: grade = "A"
elif fscore >= 0.8: grade = "B"
elif fscore >= 0.7: grade = "C"
elif fscore >= 0.6: grade = "D"
else: garde = "F"

print(grade)