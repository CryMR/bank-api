from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, database, schemas
from datetime import date
from pydantic import EmailStr, ValidationError

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

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
    
        
    return user

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
    
    return user.cards

@app.put("/cards/{card_id}")
def set_card_value(card_id: int, new_value: float, db: Session = Depends(get_db)):
    card = db.query(models.Card).filter(models.Card.id == card_id).first() 
    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    
    card.value = new_value
    db.commit()
    db.refresh(card)
    return card

@app.patch("/cards/{card_id}/upcoming")
def upcoming_money(card_id: int, amount: float, db: Session = Depends(get_db)):
    card = db.query(models.Card).filter(models.Card.id == card_id).first() 
    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    
    card.value += amount
    db.commit()
    db.refresh(card)
    return card

@app.patch("/cards/{card_id}/payment")
def payment(card_id: int, amount: float, db: Session = Depends(get_db)):
    card = db.query(models.Card).filter(models.Card.id == card_id).first() 
    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    
    if card.value < amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")
        
    card.value -= amount
    db.commit()
    db.refresh(card)
    return card

@app.patch("/cards/{card_id}/transfer")
def transfer_money(card_id: int, amount: float, target_card_id: int, db: Session = Depends(get_db)):
    source_card = db.query(models.Card).filter(models.Card.id == card_id).first() 
    target_card = db.query(models.Card).filter(models.Card.id == target_card_id).first()
    source_card_type = db.query(models.Card).filter(models.Card.id == card_id).first().type
    target_card_type = db.query(models.Card).filter(models.Card.id == target_card_id).first().type


    
    if source_card is None:
        raise HTTPException(status_code=404, detail="Source card not found")
    
    if target_card is None:
        raise HTTPException(status_code=404, detail="Target card not found")
    
    if source_card.value < amount:
        raise HTTPException(status_code=400, detail="Insufficient funds in source card")
    
    if source_card_type != target_card_type:
        raise HTTPException(status_code=400, detail="Different currencys")
        
    source_card.value -= amount
    target_card.value += amount
    
    db.commit()
    db.refresh(source_card)
    db.refresh(target_card)
    return {"message": f"Transferred {amount} from card {card_id} to card {target_card_id}"}

