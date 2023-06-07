import pandas

data = pandas.read_csv("./ListComprehension/nato_phonetic_alphabet.csv")


phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}

# versione mia
"""
errore = False

while not errore:
    word = input("Enter a word: ").upper()
    try:
        new_list = [phonetic_dict[letter] for letter in word]
        errore = True
    except KeyError:
            print("Sorry, only letters in the alphabet please.")
    else:
        print(new_list)
"""

# versione angela

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        new_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
            print("Sorry, only letters in the alphabet please.")
            generate_phonetic()
    else:
        print(new_list)

generate_phonetic()
