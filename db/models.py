from sqlalchemy import Column, Text, Integer, VARCHAR, String
from .database import Base


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String,  index=True)
    last_name = Column(String, index=True)
    patronymic = Column(String, index=True)
    phone = Column(String, index=True)
    message = Column(String, index=True)
