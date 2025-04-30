from fastapi import FastAPI
from route_teacher import router as teacher_router

app = FastAPI()
app.include_router(teacher_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Flashcard API!"}