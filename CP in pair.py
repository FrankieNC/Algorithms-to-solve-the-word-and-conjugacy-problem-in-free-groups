def string_to_pair_notation(input_string):
    pair_notation = []
    for term in input_string.split():
        generator = term[0]
        index = int(term[1:])
        
        if generator.islower():
            pair_notation.append([index, 1])
        else:
            pair_notation.append([index, -1])
    
    return pair_notation

def reduce_word(pair_notation):
    reduced_word = []

    for pair in pair_notation:
        if not reduced_word or reduced_word[-1][0] != pair[0]:
            reduced_word.append(pair)
        else:
            if reduced_word[-1][1] + pair[1] == 0:
                reduced_word.pop()
            else:
                reduced_word.append(pair)

    return reduced_word

# Define a function to cyclically reduce a word represented in pair notation
def cyclically_reduce(pair_notation):
    # Continue removing pairs from the end of the pair notation until a different index is encountered
    while pair_notation:
        last_pair = pair_notation[-1]
        pair_notation.pop()
        if not pair_notation or pair_notation[-1][0] != last_pair[0]:
            break

    # Return the cyclically reduced pair notation
    return pair_notation

# Define a function to check if two words are conjugate
def are_words_conjugate(word1, word2):
    # Convert the input words to pair notation
    pair_notation_1 = string_to_pair_notation(word1)
    pair_notation_2 = string_to_pair_notation(word2)

    # Reduce the words to their canonical form in pair notation
    reduced_form_1 = reduce_word(pair_notation_1)
    reduced_form_2 = reduce_word(pair_notation_2)

    # Cyclically reduce the words in pair notation
    cyclically_reduced_1 = cyclically_reduce(reduced_form_1)
    cyclically_reduced_2 = cyclically_reduce(reduced_form_2)

    # Check if the cyclically reduced pair notations are equal
    return cyclically_reduced_1 == cyclically_reduced_2

# Usage:
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

# Check if the words are conjugate and print the result
result = are_words_conjugate(word1, word2)
print(f"The words '{word1}' and '{word2}' are {'conjugate' if result else 'not conjugate'}.")