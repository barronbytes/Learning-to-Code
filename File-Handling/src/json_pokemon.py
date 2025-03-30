import os
import csv
import json
import copy


# paths for reading original JSON file and creating new JSON and CSV files
root_dir = os.path.dirname(os.path.relpath(__file__))
json_input_path = os.path.join(root_dir, "../data_json/pokemon.json")
json_output_path = os.path.join(root_dir, "../data_json/pokemon_new.json")
csv_output_path = os.path.join(root_dir, "../data_csv/pokemon_new.csv")


# deserialize data (read JSON file)
def read_data(file_path: str) -> dict:
    with open(file_path, mode="r") as file:
        data = json.load(file)
    return data


# update data
def update_data(data: str) -> dict:
    new_key = "psychic"
    new_value = {
        "name": "Psychic",
        "weaknesses": ["Bug", "Ghost", "Dark"],
        "strengths": ["Fighting", "Poison"],
        "immunities": [],
    }
    data["types"][new_key] = new_value
    return data


# serialize data (create JSON file)
def create_data(data: dict, file_path: str) -> None:
    with open(file_path, mode="w") as file:
        json.dump(data, file, indent=4)


# create CSV file from JSON file
def _to_csv(data: dict, file_path: str) -> None:
    with open(file_path, mode="w", newline="") as file:
        pokemon_types = list(data.keys())
        fieldnames = list(data[pokemon_types[0]].keys())
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        pokemons = []
        for pokemon_type in pokemon_types:
            row = {}
            for fn in fieldnames:
                row[fn] = data[pokemon_type][fn]
            pokemons.append(row)
        writer.writerows(pokemons)
            

# CRUd functions + convert file type
raw_data = read_data(json_input_path)
updated_data = update_data(copy.deepcopy(raw_data))
create_data(updated_data, json_output_path)
_to_csv(raw_data["types"], csv_output_path)


# print values
pokemon_types = raw_data["types"].keys()
print("\n".join(f"Type: {pt}" for pt in pokemon_types))
print("raw_data == updated_data?: ", raw_data == updated_data)