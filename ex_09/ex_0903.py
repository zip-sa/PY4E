filename = input("Enter a file name: ")

try:
    file_handle = open(filename)
except FileNotFoundError:
    print("File not found.")
    quit()

email_counts = {}  # Dictionary to store counts for each day
bigemail = None
bigcount = None

for line in file_handle:
    if line.startswith('From '):
        words = line.split()
        if len(words) > 2:
            email = words[1]
            email_counts[email] = email_counts.get(email, 0) + 1

for email, count in email_counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigemail = email
        
    
print(bigemail, bigcount)

# Print the contents of the dictionary
# print(day_counts)
