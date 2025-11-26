from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from .auth import SECRET_KEY, ALGORITHM
from .database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_company(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("company_id")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")