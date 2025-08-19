from fastapi import FastAPI
from app.api.v1 import note
from fastapi.staticfiles import StaticFiles
from app.database.database import engine
from app.models import models

models.Base.metadata.create_all(engine)
app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static") , name="static")
app.include_router(note.router)