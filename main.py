from fastapi import FastAPI, Depends, HTTPException,status
from sqlalchemy.orm import Session
from jose import JWTError, jwt

import models
import schemas
import crud
import auth

from database import engine, get_db
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    existing_username = crud.get_user_by_username(db,user.username)
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already exists")

    existing_email = crud.get_user_by_email(db,user.email)
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")

    crud.create_user(db,user)

    return {"message": "User registered successfully"}

@app.post("/login")
def login(
    user: schemas.UserLogin,
    db: Session = Depends(get_db)
):

    db_user = crud.get_user_by_username(db, user.username)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = auth.create_access_token(data={"sub": db_user.username})

    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected")
def protected(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {
            "message":"Access granted",
            "user":payload["sub"]
        }
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
