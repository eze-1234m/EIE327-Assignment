def ezekiel(word, cipher_shift_value):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    list_word = list(word.upper())

    ezekiel = list_word.copy()
    for i in range(len(list_word)):
        index = alphabet.index(list_word[i])

        index = index + cipher_shift_value
        if index > (len(alphabet) - 1):
            index = index - (len(alphabet))
            ezekiel[i] = alphabet[index]
        else:
            ezekiel[i] = alphabet[index]
    return ezekiel
print(ezekiel("Joachim", 2))
