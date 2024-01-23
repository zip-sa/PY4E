fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print("File not found.")
    quit()

unique_words = []

for line in fh:
    words = line.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

# Sort the list of unique words
unique_words.sort()

# Print the List
print(unique_words)

# Print the resulting words
#for word in unique_words:
#    print(word)
