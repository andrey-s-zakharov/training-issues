from difflib import get_close_matches
import json

# !!! Need to add any english dictionary to dictionary.json
dict_data = json.load(open("dictionary.json"))


def manage_close_matches_action(word, dict_data):
    """ Return close match for requested word or message depends on user choice """
    action = input("Did you mean {} instead? [y or n]: ".format(get_close_matches(word, dict_data.keys())[0]))
    if action == "y":
        return dict_data[get_close_matches(word, dict_data.keys())[0]]
    elif action == "n":
        return "The word doesn't exist, yet."
    else:
        return "We don't understand your entry. Apologies."


def retrieve_defenition(word):
    word = word.lower()
    if word in dict_data:
        return dict_data[word]
    elif word.title() in dict_data:
        return dict_data[word.title()]
    elif word.upper() in dict_data:
        return dict_data[word.upper()]
    elif len(get_close_matches(word, dict_data.keys())) > 0:
        return manage_close_matches_action(word, dict_data)


word_user = input("Enter a word: ")

definition = retrieve_defenition(word_user)

if type(definition) == list:
    for item in definition:
        print("-", item)
else:
    print("-", definition)
