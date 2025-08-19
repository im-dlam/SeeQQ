from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Form , status , Request , Depends 
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse , RedirectResponse
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models import models
template = Jinja2Templates('app/templates')
router = APIRouter(
    tags=["Notes"]
)
data= []
@router.get("/" , status_code=status.HTTP_200_OK)
async def homes(request: Request , db: Session =  Depends(get_db)):
    data.clear()
    for note in db.query(models.Notes).all():
        data.append(note.__dict__['note'])
    return template.TemplateResponse('index.html' , {'request':request , 'data':data})


@router.post('/add' , status_code=status.HTTP_201_CREATED)
async def add_notes(item_note: Optional[str] = Form(...), db: Session =  Depends(get_db)):
    now_time = datetime.now()
    user_id = 1
    q = models.Notes(note=item_note,datetime=now_time,user_id=user_id)
    db.add(q)
    db.commit()
    db.refresh(q)

    return RedirectResponse('/',status_code=302)

@router.get("/my-notes" , status_code=status.HTTP_200_OK)
async def my_notes(request: Request):
    return template.TemplateResponse('note.html' , {'request':request , 'notes':data})