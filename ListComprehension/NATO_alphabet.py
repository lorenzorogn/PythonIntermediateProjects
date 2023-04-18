import pandas

data = pandas.read_csv("./ListComprehension/nato_phonetic_alphabet.csv")
new_dict = {row.letter:row.code for (index,row) in data.iterrows()}
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()

new_list = [new_dict[letter] for letter in word]

print(new_list)



