from sqlalchemy.orm import Session
from datetime import datetime
import models, schemas, security
#traemos user por su email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

#creamos user de acuerdo al modelo
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = security.get_password_hash(user.password)
    now = datetime.utcnow()
    
    db_user = models.User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password,
        created=now,
        modified=now,
        last_login=now
    )
    db.add(db_user)
    
    # crear y asociar los telefonos
    if user.phones:
        for phone_data in user.phones:
            db_phone = models.Phone(**phone_data.dict(), owner=db_user)
            db.add(db_phone)
            
    db.commit()
    db.refresh(db_user)
    return db_user

    #actualizamos token
def update_user_token(db: Session, user_id: str, token: str):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db_user.token = token
        db.commit()
        db.refresh(db_user)
    return db_user
