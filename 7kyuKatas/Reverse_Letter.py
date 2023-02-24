
def reverse_letter(word):

    rev_word = word[::-1]

    alphabetic_list = []
    
    for character in rev_word:
        if character.isalnum() and not character.isdigit():
            alphabetic_list.append(character)
    final_word = ''.join(alphabetic_list)
    
    return final_word
