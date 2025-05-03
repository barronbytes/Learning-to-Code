from schema_deck import Deck
import model_database # ensure shared db is modified


def create_deck(name: str) -> Deck:
    deck = Deck(deck_id=name, cards=[])
    model_database.db[name] = deck
    return deck


def read_deck(name: str) -> Deck:
    deck = model_database.db.get(name)
    return deck
