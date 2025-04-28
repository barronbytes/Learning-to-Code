from typing import Union
from fastapi import HTTPException
from model_card import Card
from database import decks


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
