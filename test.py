""" import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex) """

""" print(data[0]) """

""" for index, item in enumerate(data):
    print(index, ":", item["name"]) """

""" import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
choice = input("Pick a language from chinese, english, japanese, french: ")
for index, item in enumerate(data):
    if choice == "chinese":
        print(f"{index}: {item["name"]["chinese"]}")
    if choice == "english":
        print(f"{index}: {item["name"]["english"]}")
    if choice == "japanese":
        print(f"{index}: {item["name"]["japanese"]}")
    if choice == "french":
        print(f"{index}: {item["name"]["french"]}") """

"""import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
choice = input("What type do you want: ")
for index, item in enumerate(data):
    if choice in ["type"]:
        print(f"{index}: {item["name"]["english"]}") """
 
""" import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
choice = input("What pokemon do you want: ")
for index, item in enumerate(data):
    if choice in (f"{index}: {item["name"]["english"]}"):
        print(f"{index}: {item["name"]["english"]}")
else:
    print("No pokemon found") """

import json
pokedex = open("./pokedex.json", encoding="utf8")
moves = open("./moves.json", encoding="utf8")
data = json.load(pokedex)
data_2 = json.load(moves)
choice = input("What pokemon do you want: ")
for index, item in enumerate(data):
    if choice in (f"{index}: {item["name"]["english"]}"):
        print(f"{index}: {item["name"]["english"]}")
        print(f"{index}: {item["type"]}")
for index, item in enumerate(data_2):
    poke_types = item['type']
for move in data_2:
    if move['type'] in poke_types:
        print(f"{move['ename']} ({move['type']})")