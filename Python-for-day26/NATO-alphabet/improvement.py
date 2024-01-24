import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_data = {row.letter: row.code for (index, row) in data.iterrows()}


def generate():
    user_enter = input("Enter a word:").upper()

    # check if the input exists in alphabet, so we should try to check the input value
    # and then compare the value with the key in dict
    # if it not exists, print out something
    try:
        words = [new_data[letter] for letter in user_enter]
    except KeyError:
        print("Sorry, only letters in the NATO alphabet are allowed.")
        generate()
    else:
        print(words)


generate()
