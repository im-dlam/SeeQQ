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
@router.get('/all-notes' , status_code=status.HTTP_200_OK)
async def all_notes(db: Session =  Depends(get_db)):
    # print(db.query(models.Notes).all())
    return db.query(models.Notes).all()


@router.get("/" , status_code=status.HTTP_200_OK)
async def homes(request: Request , db: Session =  Depends(get_db)):
    data = db.query(models.Notes).all()
    return template.TemplateResponse('create_list.html' , {'request':request , 'data':data})


@router.post('/create-note' , status_code=status.HTTP_201_CREATED)
async def add_notes(note_name: Optional[str] = Form(...), note_descriptions: Optional[str] = Form(...), db: Session =  Depends(get_db)):
    notes = models.Notes(note_name=note_name,note_descriptions=note_descriptions, datetime=datetime.now())
    db.add(notes)
    db.commit()
    db.refresh(notes)
    return RedirectResponse(f'/list-notes/{notes.id}',status_code=302)
@router.post('/delete-note' , status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(note_id: Optional[str] = Form(...),note_content: Optional[str] = Form(...), db: Session = Depends(get_db)):
    deleting = db.query(models.Notes).filter(models.Notes.id == note_id and models.Notes.note == note_content)
    deleting.delete(synchronize_session=False)
    db.commit()
    return {'status':200}

@router.get("/list-notes/{id}" , status_code=status.HTTP_200_OK)
async def my_notes(request: Request,id: int, db: Session =  Depends(get_db)):
    data = db.query(models.Notes).filter(models.Notes.id == id).first()

    status_code = status.HTTP_200_OK if data else status.HTTP_404_NOT_FOUND
    
    return template.TemplateResponse('list_notes.html' , {'request':request , 'note':data}, status_code=status_code)
    