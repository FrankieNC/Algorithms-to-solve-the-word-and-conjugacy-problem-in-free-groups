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

def are_words_equal(word1, word2):
    pair_notation_1 = string_to_pair_notation(word1)
    pair_notation_2 = string_to_pair_notation(word2)

    reduced_form_1 = reduce_word(pair_notation_1)
    reduced_form_2 = reduce_word(pair_notation_2)

    return reduced_form_1 == reduced_form_2

# Example usage:
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

result = are_words_equal(word1, word2)
print(f"The words '{word1}' and '{word2}' are {'equal' if result else 'not equal'}.")
