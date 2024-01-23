import string

def count_letter_frequency(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()  # Convert to lowercase
    except FileNotFoundError:
        print("File not found.")
        return

    letter_counts = {}
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            letter_counts[char] = letter_counts.get(char, 0) + 1
    
    # Sort the letters by frequency in descending order
    sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

    # Print the result
    for letter, count in sorted_letters:
        print(f'{letter}: {count}')

# Example usage:
filename = input("Enter the file name: ")
count_letter_frequency(filename)
