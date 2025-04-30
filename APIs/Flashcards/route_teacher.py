from fastapi import APIRouter
from schema_deck import Deck
from service_lesson import create_lesson, read_lessons


router = APIRouter(prefix="/teacher", tags=["Teacher"])


# use plural nouns for resources
@router.post(path="/lessons")
def create_lesson_route(name: str) -> dict[str, list]:
    return create_lesson(name)


@router.get(path="/lessons")
def read_lessons_route() -> dict[str, list]:
    return read_lessons()
