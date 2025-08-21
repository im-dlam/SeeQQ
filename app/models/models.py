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
    # user_id = Column(Integer, ForeignKey('users.id')) # Khóa ngoại của bảng users

    # creator = relationship('User',back_populates='notes')

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String)
    password =  Column(String)

    # notes = relationship('Notes', back_populates='creator')