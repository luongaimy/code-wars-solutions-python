def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""

    for i in range(len(string_)):
        if string_[i] not in vowels:
            result = result + string_[i]

    return result