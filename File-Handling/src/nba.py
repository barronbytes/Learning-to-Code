import os
import csv
import json
import copy


# CSV -> read, update -> create JSON
root_dir = os.path.dirname(os.path.relpath(__file__))
csv_input_path = os.path.join(root_dir, "../data_csv/nba.csv")
csv_output_path = os.path.join(root_dir, "../data_csv/nba_new.csv")
json_output_path = os.path.join(root_dir, "../data_json/nba.json")


# deserialize data (read file)
def read_data(file_path: str) -> dict:
    with open(file_path, mode="r") as file:
        reader = csv.reader(file)
        data = list(reader)
    return data


# update data
def update_data(data: list[list[str]]) -> list[list[str]]:
    new_row = ["San Antonio Spurs", "West", "5"]
    data.append(new_row)
    return data


# serialize data (create file)
def create_data(data: list[list[str]], file_path: str) -> None:
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)


# CRUd functions + convert file type
raw_data = read_data(csv_input_path)
updated_data = update_data(copy.deepcopy(raw_data))
create_data(updated_data, csv_output_path)