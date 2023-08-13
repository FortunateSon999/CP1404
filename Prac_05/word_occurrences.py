"""
CP1404/CP5632 Practical
word_occurrences.py
Estimate: 15minutes
Actual:
"""
def count_word_occurrences(text):
    words_dictionary = {}
    words = text.split()
    for word in words:
        word = word.lower()  # Convert word to lowercase for case-insensitive counting
        words_dictionary[word] = words_dictionary.get(word, 0) + 1
    return words_dictionary

def main():
    user_input = input("Enter a string: ")
    word_counts = count_word_occurrences(user_input)

    # Find the length of the longest word for alignment
    max_word_length = max(len(word) for word in word_counts)

    # Print the counts with aligned output
    for word, count in sorted(word_counts.items()):
        print(f"{word:{max_word_length}} : {count}")

main()
