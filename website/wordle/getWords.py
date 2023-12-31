import random


def words():
    with open('website/wordle/words.txt') as f:
        word_list = f.readlines()
        return random.choice(word_list)[0:5]
