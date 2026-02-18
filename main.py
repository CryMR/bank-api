from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, database, schemas
from datetime import date
from pydantic import EmailStr, ValidationError

# Создаем таблицы (в реальных проектах лучше использовать Alembic)
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Функция-зависимость для получения сессии БД
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user(name: str, email: EmailStr, date_of_birth: date, phone_number: str = None, db: Session = Depends(get_db)):
    db_user = models.User(name=name, email=email, date_of_birth=date_of_birth, phone_number=phone_number)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first() 
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
        
    return user # FastAPI сам возьмет 'user', вычислит 'age' и превратит в JSON по схеме

@app.post("/cards/")
def create_card(owner_id: int, card_number: str, value: float, type: str, db: Session = Depends(get_db)):
    db_card = models.Card(owner_id=owner_id, card_number=card_number, value=value, type=type)
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card

@app.get("/cards/{card_id}", response_model=schemas.CardResponse)
def read_card(card_id: int, db: Session = Depends(get_db)): 
    card = db.query(models.Card).filter(models.Card.id == card_id).first() 
    
    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    
    return card

@app.get("/users/{user_id}/cards", response_model=list[schemas.CardResponse])
def read_user_cards(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first() 
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user.cards  # FastAPI сам превратит список карт в JSON по схеме

