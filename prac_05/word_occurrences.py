"""
Word Occurrences NEW
Estimate: 40 minutes
Actual:   38 minutes
"""


def main():
    """Program to count word occurrences in a text sentence."""
    sentence_text = input("Enter a string: ").split()
    words_to_occurrences = {}
    for word in (sorted(sentence_text)):
        if word in words_to_occurrences:
            # If word already exists in dictionary, add 1 to the value of the respective key
            words_to_occurrences[word] += 1
        else:
            # If word does not exist, the dictionary creates/initialises the word and sets the value (occurrences) to 1
            words_to_occurrences[word] = 1
    max_width = max(len(word) for word in sentence_text)
    # Finds the length of each word in sentence_text then gets the max of those int values
    for word, count in words_to_occurrences.items():
        print(f"{word:{max_width}} : {count}")


main()
