dict = {
    'Pokemon': 'Pikachu', 
    'Digimon': 'Agumon', 
    'Yugioh': 'Black Magician'
}

word = input()

if word in dict:
    print(dict[word])
else:
    print("I don't know")