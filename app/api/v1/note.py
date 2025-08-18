from typing import Optional
from fastapi import APIRouter, Form , status , Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse , RedirectResponse

template = Jinja2Templates('app/templates')
router = APIRouter(
    tags=["Notes"]
)
data= []
@router.get("/" , status_code=status.HTTP_200_OK)
async def homes(request: Request):
    print(data)
    return template.TemplateResponse('index.html' , {'request':request , 'data':data})


@router.post('/add' , status_code=status.HTTP_201_CREATED)
async def add_notes(item_note: Optional[str] = Form(...)):
    data.append(item_note)
    return RedirectResponse('/',status_code=302)

@router.get("/my-notes" , status_code=status.HTTP_200_OK)
async def homes(request: Request):
    return template.TemplateResponse('note.html' , {'request':request , 'notes':data})