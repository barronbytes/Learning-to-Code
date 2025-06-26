"""
O(1) — Constant Time

"""

# Dictionary: first name → last name
names_dict = {
    "Alice": "Smith",
    "Bob": "Johnson",
    "Charlie": "Brown"
}

# Function to print the last name
def print_last_name(fname: str) -> None:
    print(f"last name: {names_dict[fname]}")

print_last_name("Alice")