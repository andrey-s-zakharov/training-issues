import itertools as it
import random


ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suits = ['C', 'D', 'H', 'S']


def form_cards_deck(ranks, suits):
    """ Return iterator over tuples of cards deck """
    return it.product(ranks, suits)


def shuffle(deck):
    """ Return iterator over shuffled deck """
    deck = list(deck)
    random.shuffle(deck)
    return iter(tuple(deck))


def cut(deck, n):
    """ Return iterator over cards deck cut an index n """
    deck_1, deck_2 = it.tee(deck, 2)
    top = it.islice(deck_1, n)
    bottom = it.islice(deck_2, n, None)
    return it.chain(bottom, top)


def deal(deck, num_hands=1, hand_size=5):
    """ Divide cards deck between players """
    iters = [iter(deck)] * hand_size
    return tuple(zip(*(tuple(it.islice(itr, num_hands)) for itr in iters)))


# Examples results of functions

# Form deck of cards
deck = form_cards_deck(ranks, suits)
print([card for card in form_cards_deck(ranks, suits)])
'''
[
    ('A', 'H'), ('A', 'D'), ('A', 'C'), ('A', 'S'), ('K', 'H'), ('K', 'D'), ('K', 'C'),
    ('K', 'S'), ('Q', 'H'), ('Q', 'D'), ('Q', 'C'), ('Q', 'S'), ('J', 'H'), ('J', 'D'),
    ('J', 'C'), ('J', 'S'), ('10', 'H'), ('10', 'D'), ('10', 'C'), ('10', 'S'), ('9', 'H'),
    ('9', 'D'), ('9', 'C'), ('9', 'S'), ('8', 'H'), ('8', 'D'), ('8', 'C'), ('8', 'S'), ('7', 'H'),
    ('7', 'D'), ('7', 'C'), ('7', 'S'), ('6', 'H'), ('6', 'D'), ('6', 'C'), ('6', 'S'), ('5', 'H'),
    ('5', 'D'), ('5', 'C'), ('5', 'S'), ('4', 'H'), ('4', 'D'), ('4', 'C'), ('4', 'S'), ('3', 'H'),
    ('3', 'D'), ('3', 'C'), ('3', 'S'), ('2', 'H'), ('2', 'D'), ('2', 'C'), ('2', 'S')
]
'''
# Shuffle cards
shuffled_deck = shuffle(deck)
#print([card for card in shuffled_deck])

# One of the variants of shufflе
'''
[
    ('5', 'D'), ('A', 'D'), ('Q', 'S'), ('2', 'C'), ('2', 'H'), ('4', 'H'), ('3', 'C'), ('6', 'S'),
    ('2', 'D'), ('7', 'D'), ('10', 'H'), ('9', 'H'), ('J', 'C'), ('9', 'S'), ('3', 'D'), ('10', 'S'),
    ('4', 'S'), ('K', 'H'), ('3', 'H'), ('Q', 'H'), ('8', 'H'), ('A', 'C'), ('7', 'S'), ('J', 'S'),
    ('4', 'C'), ('6', 'H'), ('Q', 'C'), ('2', 'S'), ('5', 'S'), ('4', 'D'), ('10', 'D'), ('3', 'S'),
    ('8', 'D'), ('A', 'S'), ('A', 'H'), ('9', 'C'), ('6', 'D'), ('K', 'S'), ('6', 'C'), ('9', 'D'),
    ('7', 'H'), ('8', 'S'), ('Q', 'D'), ('5', 'C'), ('K', 'D'), ('J', 'D'), ('8', 'C'), ('K', 'C'),
    ('5', 'H'), ('J', 'H'), ('10', 'C'), ('7', 'C')
]
'''
# Cut card by random value
cutted_deck = cut(shuffled_deck, 20)
# print([card for card in cutted_deck])
'''
[
    ('3', 'D'), ('5', 'S'), ('6', 'D'), ('8', 'S'), ('A', 'H'), ('5', 'C'), ('3', 'H'), ('7', 'C'),
    ('3', 'S'), ('9', 'C'), ('8', 'D'), ('Q', 'S'), ('4', 'S'), ('J', 'D'), ('8', 'H'), ('2', 'D'),
    ('4', 'H'), ('6', 'S'), ('Q', 'C'), ('A', 'D'), ('9', 'S'), ('4', 'C'), ('5', 'H'), ('4', 'D'),
    ('A', 'S'), ('10', 'C'), ('K', 'H'), ('J', 'H'), ('10', 'H'), ('3', 'C'), ('6', 'H'), ('Q', 'D'),
    ('2', 'S'), ('9', 'H'), ('7', 'D'), ('8', 'C'), ('K', 'S'), ('9', 'D'), ('Q', 'H'), ('10', 'D'),
    ('J', 'C'), ('7', 'H'), ('2', 'H'), ('K', 'D'), ('2', 'C'), ('J', 'S'), ('10', 'S'), ('K', 'C'),
    ('5', 'D'), ('6', 'C'), ('7', 'S'), ('A', 'C')
]
'''
# Deal cards between players
player_1_hand, player_2_hand, player_3_hand = deal(cutted_deck, num_hands=3)
print(player_1_hand)
print(player_2_hand)
print(player_3_hand)
'''
(('9', 'D'), ('2', 'H'), ('Q', 'S'), ('Q', 'H'), ('K', 'S'))
(('4', 'S'), ('K', 'D'), ('4', 'H'), ('K', 'C'), ('7', 'C'))
(('9', 'S'), ('4', 'D'), ('Q', 'C'), ('9', 'C'), ('K', 'H'))
'''
# Length of cutted deck of cards after deal
print(len(tuple(cutted_deck)))
''' 37 ''' # -15 cards for players
