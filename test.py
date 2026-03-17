import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)

""" print(data[0]) """

""" for index, item in enumerate(data):
    print(index, ":", item["name"]) """

