# O(1) — Constant Time


def print_last_name(fname: str) -> None:
    print(f"last name: {names_dict[fname]}")


names_dict = {
    "Alice": "Smith",
    "Bob": "Johnson",
    "Charlie": "Brown"
}
print_last_name("Alice")
