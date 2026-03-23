""" import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex) """

""" print(data[0]) """

""" for index, item in enumerate(data):
    print(index, ":", item["name"]) """

""" import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex) """
""" choice = input("Pick a language from chinese, english, japanese, french: ")
for index, item in enumerate(data):
    if choice == "chinese":
        print(f"{index}: {item["name"]["chinese"]}")
    if choice == "english":
        print(f"{index}: {item["name"]["english"]}")
    if choice == "japanese":
        print(f"{index}: {item["name"]["japanese"]}")
    if choice == "french":
        print(f"{index}: {item["name"]["french"]}") """

import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
choice = input("What type do you want: ")
for index, item in enumerate(data):
    if choice == "bug" and 
        print(f"{index}: {item["name"]["english"]}")
