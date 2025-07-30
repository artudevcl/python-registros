from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta

import crud, models, schemas, security
from database import SessionLocal, engine, create_db_and_tables

#creaBD
create_db_and_tables()

app = FastAPI()

# depedencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Posteo para registro usuario
@app.post("/users/register", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    #error del correo existent
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo ya registrado",
        )
    
    created_user = crud.create_user(db=db, user=user)
    #expiracion del token
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": created_user.email}, expires_delta=access_token_expires
    )
    
    crud.update_user_token(db=db, user_id=created_user.id, token=access_token)
    #respuesta a la solicitud
    response_data = schemas.UserResponse(
        id=created_user.id,
        created=created_user.created,
        modified=created_user.modified,
        last_login=created_user.last_login,
        token=access_token,
        isactive=created_user.is_active
    )
    
    return response_data
