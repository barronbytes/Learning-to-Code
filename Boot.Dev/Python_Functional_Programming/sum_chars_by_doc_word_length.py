from functools import reduce

def sum_chars_by_doc_word_length(document):
    """
    Calculates the total number of characters in words with at least five characters in a words document.

    Parameters:
        document (str): A document string.

    Returns:
        int: The total number of characters in words with a length of 5 or more characters.

    Examples:
    >>> sum_chars_by_doc_word_length("Python is amazing. It allows for simple and powerful programming. Explore its features!")
    62
    >>> sum_chars_by_doc_word_length("Hello world!")
    11
    """

    words = document.split()

    lowercase_words = map(lambda word: word.lower(), words)
    filtered_words = filter(lambda word: not len(word) < 5, lowercase_words)
    total_characters = reduce(lambda sum, word: sum + len(word),filtered_words, 0)
    return total_characters
