def getColors(g_word, n_word):

    n_word = n_word.upper()
    g_word = g_word.upper()

    colors = ['', '', '', '', '']

    word_hashmap = {}

    for i in g_word:
        if i not in word_hashmap:
            word_hashmap[i] = 1
        else:
            word_hashmap[i] += 1

    for index, letter in enumerate(n_word):
        if letter == g_word[index]:
            colors[index] = 'green'

            if word_hashmap[letter] > 1:
                word_hashmap[letter] -= 1
            else:
                del word_hashmap[letter]

    for index, letter in enumerate(n_word):
        if colors[index] == '':
            if letter in word_hashmap:
                colors[index] = 'yellow'

                if word_hashmap[letter] > 1:
                    word_hashmap[letter] -= 1
                else:
                    del word_hashmap[letter]

            else:
                colors[index] = 'white'

    return [[n_word[0], n_word[1], n_word[2], n_word[3], n_word[4]], colors]
