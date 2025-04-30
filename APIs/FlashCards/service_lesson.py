from schema_lesson import Lesson
from model_flashcards import lesson_id, flashcards


def read_lesson(id: int) -> Lesson:
    return flashcards[id]
