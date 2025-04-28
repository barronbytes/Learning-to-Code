from model_deck import Deck
from fastapi import HTTPException


decks: list[Deck] = []
id_counter: int = 0


def create_deck(name: str) -> Deck:
    global id_counter
    if any(deck.name == name for deck in decks):
        raise HTTPException(status_code=409, detail="Deck already exists.")
    new_deck = Deck(id=id_counter, name=name)
    id_counter += 1
    decks.append(new_deck)
    return new_deck


def get_deck(id: int) -> Deck:
    deck = next((deck for deck in decks if deck.id == id), None)
    if not deck:
        raise HTTPException(status_code=404, detail="Deck not found.")
    return deck


def update_deck(id: int, new_name: str) -> Deck:
    deck = next((deck for deck in decks if deck.id == id), None)
    if not deck:
        raise HTTPException(status_code=404, detail="Deck not found.")
    deck.name = new_name
    return deck


def delete_deck(id: int) -> Deck:
    deck = next((deck for deck in decks if deck.id == id), None)
    if not deck:
        raise HTTPException(status_code=404, detail="Deck not found.")
    decks.remove(deck)
    return deck
