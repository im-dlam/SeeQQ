import os , sys

import uvicorn

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from app.api.v1 import note


app = FastAPI()

app.include_router(note.router)

if __name__ == '__main__':
    os.system('uvicorn app.main:app --reload')