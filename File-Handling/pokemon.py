import json
import copy


file_path = "pokemon_types.json"


# serialize data (create file)
def create_data(data: dict, file_path: str) -> None:
    with open(file_path, mode="w") as new_file:
        json.dump(data, new_file, indent=4)


# deserialize data (read file)
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


raw_data = read_data(file_path)
updated_data = update_data(copy.deepcopy(raw_data))
create_data(updated_data, file_path)

pokemon_types = raw_data["types"].keys()
print("\n".join(f"Type: {d}" for d in pokemon_types))
print(raw_data == updated_data)