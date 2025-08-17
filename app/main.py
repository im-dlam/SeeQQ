from fastapi import FastAPI
from app.api.v1 import note
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static") , name="static")
app.include_router(note.router)