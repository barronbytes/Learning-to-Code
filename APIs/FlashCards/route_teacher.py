from typing import Union
from fastapi import APIRouter, HTTPException
from service_deck import create_deck, get_deck, update_deck, delete_deck
from service_card import create_card
from model_deck import Deck
from model_card import Card


router = APIRouter(prefix="/teacher", tags=["Teacher"])


@router.post("/deck/", response_model=Deck)
def create_deck_route(name: str) -> Deck:
    return create_deck(name)


@router.get("/deck/{id}", response_model=Deck)
def get_deck_route(id: int) -> Deck:
    return get_deck(id)


@router.put("/deck/{id}", response_model=Deck)
def update_deck_route(id: int, new_name: str) -> Deck:
    return update_deck(id, new_name)


@router.delete("/deck/{id}", response_model=Deck)
def delete_deck_route(id: int) -> Deck:
    return delete_deck(id)


@router.post("/deck/{name}/card", response_model=Card)
def create_card_route(name: str, question: Union[str, int], answer: Union[str, int], tags: list[str]) -> Card:
    return create_card(name, question, answer, tags)