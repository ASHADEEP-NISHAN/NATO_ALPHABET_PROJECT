import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(dict)

def generate_phonetic():
    user_input = input("what is your name :").upper()
    try:
        output_list = [dict[letter] for letter in user_input]
    except KeyError:
        print("sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output_list)
generate_phonetic()
