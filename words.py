def print_upper_words(words):
    """For a list of words, print out each word on a separate line, but in all uppercase."""

    for word in words:
        print(word.upper())

def print_upper_words_e(words):
    """For a list of words, print out each word on a separate line, but in all uppercase but only if they start with e/E"""

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words_params(words, params):
    """For a list of words, you should be able to pass in a set of letters, and it only prints words that start with one of those letters."""

    for word in words:
        for letter in params:
            if word.startswith(letter):
                print(word.upper())