from fastapi import APIRouter
from schema_lesson import Lesson
from service_lesson import create_lesson, read_lesson


router = APIRouter(prefix="/teacher", tags=["Teacher"])


# use plural nouns for resources
@router.post(path="/lessons", response_model=Lesson)
def create_lesson_route() -> Lesson:
    return create_lesson()


@router.get(path="/lessons/{id}", response_model=Lesson)
def read_lesson_route(id: int) -> Lesson:
    return read_lesson(id)
