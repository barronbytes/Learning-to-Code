import json


file_path = "pokemon_types.json"
new_file_path = "updated_pokemon_types.json"


# reading (deserializing) data
def read_file(file_path: str) -> dict:
    with open(file_path, mode="r") as file:
        data = json.load(file)
    return data


# serializing data
def create_file(data: dict, new_file_path: str) -> None:
    with open(new_file_path, mode="w") as new_file:
        json.dump(data, new_file, indent=4)


pokemon_data = read_file(file_path)
pokemon_types = pokemon_data["types"].keys()
print("\n".join(f"Type: {d}" for d in pokemon_types))
