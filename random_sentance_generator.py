import variables
import random


def get_random_word(words):
    return random.choice(words)


print("Hello, this is Random Sentance Generator !")
input(f'Click [Enter] to generate your first sentence.')

while True:
    random_name = get_random_word(variables.names)
    random_place = get_random_word(variables.places)
    random_verb = get_random_word(variables.verbs)
    random_noun = get_random_word(variables.nouns)
    random_adverb = get_random_word(variables.adverbs)
    random_detail = get_random_word(variables.details)
    print(f'{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}.')
    input(f'Click [Enter] to generate a new one!')
