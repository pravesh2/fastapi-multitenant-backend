from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, auth
from ..dependencies import get_db

router = APIRouter(prefix="/users")

@router.post("/register")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed = auth.hash_password(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed, company_id=1)
    db.add(db_user)
    db.commit()
    return {"msg": "User created"}

@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        return {"error": "Invalid credentials"}
    token = auth.create_token({"company_id": db_user.company_id})
    return {"access_token": token}