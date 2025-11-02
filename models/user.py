from sqlalchemy import Column, Integer, String, Text, LargeBinary, DECIMAL, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    firebase_uid = Column(String(100), unique=True, nullable=False)
    email = Column(String(100))
    name = Column(String(100))
    address = Column(String(255))
    phone = Column(String(20))