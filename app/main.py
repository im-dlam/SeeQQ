from fastapi import FastAPI
from app.api.v1 import note


app = FastAPI()

app.include_router(note.router)