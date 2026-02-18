from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from database import Base
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import date
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    date_of_birth = Column(Date)
    phone_number = Column(String)
    
    @hybrid_property
    def age(self):
        today = date.today()
        # Вычисляем разницу лет, учитывая, был ли уже день рождения в этом году
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )
    
    cards = relationship("Card", back_populates="users")  # Связь с картами

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))  # В реальной модели нужно сделать ForeignKey
    card_number = Column(String, unique=True, index=True)
    value = Column(Float)
    type = Column(String)

    users = relationship("User", back_populates="cards")