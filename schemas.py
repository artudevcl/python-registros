import re
from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import datetime
from uuid import UUID

# Regex para validar el correo
EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.cl$"
# Regex para la clave: Una mayúscula, letras minúsculas y dos números
PASSWORD_REGEX = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d.*\d)[A-Za-z\d@$!%*?&]{8,}$"


class PhoneBase(BaseModel):
    number: str
    citycode: str
    contrycode: str

class UserCreate(BaseModel):
    name: str
    email: str = Field(..., example="usuario@dominio.cl")
    password: str = Field(..., example="PassWord12")
    phones: Optional[List[PhoneBase]] = None
#validadores de pydantic email
    @validator('email')
    def validate_email(cls, v):
        if not re.match(EMAIL_REGEX, v):
            raise ValueError("Formato de correo inválido. Debe ser aaaaaaa@dominio.cl")
        return v
#validadores de pydantic clave
    @validator('password')
    def validate_password(cls, v):
        if not re.match(PASSWORD_REGEX, v):
            raise ValueError("La contraseña no cumple con los requisitos: una mayúscula, minúsculas y dos números.")
        return v

class UserResponse(BaseModel):
    id: UUID
    created: datetime
    modified: datetime
    last_login: datetime
    token: str
    isactive: bool

    class Config:
        from_attributes = True 
