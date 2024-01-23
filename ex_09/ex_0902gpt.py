filename = input("Enter a file name: ")

try:
    file_handle = open(filename)
except FileNotFoundError:
    print("File not found.")
    quit()

day_counts = {}  # Dictionary to store counts for each day

for line in file_handle:
    if line.startswith('From '):
        words = line.split()
        if len(words) > 2:
            day = words[2]
            day_counts[day] = day_counts.get(day, 0) + 1

# Print the contents of the dictionary
print(day_counts)
