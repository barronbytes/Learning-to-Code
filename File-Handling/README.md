# File Handling

Data can be stored in different formats, and this repository demonstrates how to read, write, and convert between them. The project utilizes the modules `os`, `csv`, `json`, and `copy` to handle the data operations.

## CSV Data

The **nba.py** file was used to do the following:
* **read_data():** Read file with **csv.reader()** method.
* **update_data():** Create **deep copy** of orignal data to update
* **create_data():** Write file with **csv.writer()** and **writer.writerows()** methods.
* **map_to_json():** Uses **json.dump()** method to complete conversion to JSON data.
