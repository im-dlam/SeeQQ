from typing import Optional
from fastapi import APIRouter, Form , status , Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse , RedirectResponse

template = Jinja2Templates('app/templates')
router = APIRouter(
    tags=["Notes"]
)

@router.get("/" , status_code=status.HTTP_200_OK)
async def homes(request: Request):
    return template.TemplateResponse('index.html' , {'request':request})


@router.post('/add' , status_code=status.HTTP_201_CREATED)
async def add_notes(item_note: Optional[str] = Form(...)):
    return {'text':item_note}