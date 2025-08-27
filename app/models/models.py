import datetime
from app.database.database import Base
from sqlalchemy import Column, String , Integer , ForeignKey , Date
from sqlalchemy.orm import relationship

class Notes(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(Date)
    note_name = Column(String)
    note_descriptions = Column(String)

    work = relationship('Works', back_populates='notes')
class Works(Base):
    __tablename__ = 'works'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    datetime = Column(Date)
    note_id = Column(Integer , ForeignKey('notes.id'))
    notes = relationship('Notes', back_populates='work')
    
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String)
    password =  Column(String)

    # notes = relationship('Notes', back_populates='creator')