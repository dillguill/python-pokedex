import requests

while True:
    pokedex = input("Search Pokédex: ")
    pokedex = pokedex.lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{pokedex}"

    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
        print(f"Name is\t{data['name']}")
        print("Type:")
        for types in data['types']:
            print(types['type']['name'])
        print("Abilities:")
        for ability in data['abilities']:
            print(ability['ability']['name'])
        print 
    else:
        print("Pokémon Not Found")

