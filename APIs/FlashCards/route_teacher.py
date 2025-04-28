from typing import Union
from fastapi import APIRouter, HTTPException
from model_card import Card
from model_deck import Deck


router = APIRouter(prefix="/teacher", tags=["Teacher"])
decks: list[Deck] = []
id: int = 0


@router.post("/deck/", response_model=Deck)
def create_deck(name: str) -> Deck:
    global id
    if any(deck.name == name for deck in decks):
        raise HTTPException(status_code=409, detail="Deck already exists.")
    new_deck = Deck(id=id, name=name)
    id += 1
    decks.append(new_deck)
    return new_deck


@router.post("/deck/{name}/card", response_model=Card)
def create_card(name: str, question: Union[str, int], answer: Union[str, int], tags: list[str]) -> Card:
    new_card = Card(question=question, answer=answer, tags=tags)
    deck = next((deck for deck in decks if deck.name == name), None)
    if not deck:
        raise HTTPException(status_code=404, detail="Deck not found.")
    if any(
        card.question == question and card.answer == answer and card.tags == tags
        for card in deck.pairs
    ):
        raise HTTPException(status_code=409, detail="Card already exists.")
    deck.pairs.append(new_card)
    return new_card

        
@router.get("/deck/{id}", response_model=Deck)
def get_deck(id: int) -> Deck:
    deck = next((deck for deck in decks if deck.id == id), None)
    if not deck:
        raise HTTPException(status_code=404, detail="Deck not found.")
    return deck



@router.put("/deck/{id}", response_model=Deck)
def update_deck(id: int, new_name: str) -> Deck:
    deck = next((deck for deck in decks if deck.id == id), None)
    if not deck:
        raise HTTPException(status_code=404, detail="Deck not found.")
    deck.name = new_name
    return deck


@router.delete("/deck/{name}", response_model=Deck)
def delete_deck(name: str) -> Deck:
    deck = next((deck for deck in decks if deck.name == name), None)
    if not deck:
        raise HTTPException(status_code=404, detail="Deck not found.")
    decks.remove(deck)    
    return deck
