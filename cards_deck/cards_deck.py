import itertools as it
import random


ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suits = ['H', 'D', 'C', 'S']


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
    top = it.slice(deck_1, n)
    bottom = it.slice(deck_2, n, None)
    return it.chain(bottom, top)


def deal(deck, num_hands=1, hand_size=5):
    """ divide cards deck between players """
    iters = [iter(deck)] * hand_size
    return tuple(zip(*(tuple(it.islice(itr, num_hands)) for itr in iters)))


# Examples results of functions

# form_cards_deck(ranks, suits)
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


