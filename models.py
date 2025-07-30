from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

# importamos base desde database.py
from database import Base


#modelo clase usuario como se pidieron
class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    last_login = Column(DateTime, nullable=False)
    token = Column(String)
    is_active = Column(Boolean, default=True)
    
    phones = relationship("Phone", back_populates="owner")
#modelo clase telefono 
class Phone(Base):
    __tablename__ = "phones"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    number = Column(String)
    citycode = Column(String)
    contrycode = Column(String)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="phones")
