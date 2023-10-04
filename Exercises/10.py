# 10. Write a Python function that takes a string as input and returns a new string where each word in the string is replaced with the word that appears most frequently in the string.

def replace_with_most_frequent_word(input_str):
    
    # change the input string into words
    words = input_str.split()
    print(f"The words: {words}\n")

    # couting the occurence of each words
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    print(f"{word_count}\n")

    # finding the most frequent word
    most = ""
    max_freq = 0
    for word in word_count:
        if word_count[word] > max_freq:
            most = word
            max_freq = word_count[word]
    print(f"Most frequent word : {most} with frequency: {max_freq}\n")

    # replacing all other words with the most frequent word
    replace = ""
    for word in words:
        replace += most + " "

    print(f"The replaced string: {replace}" )

replace_with_most_frequent_word("I love python and python also loves me")