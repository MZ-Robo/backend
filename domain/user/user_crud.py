from sqlalchemy.orm import Session
from models import User as UserModel
from domain.user.user_schema import UserCreate


def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(UserModel).filter(UserModel.username == username).first()


def create_user(db: Session, user: UserCreate):
    hashed_password = user.password  # You should hash the password before saving
    db_user = UserModel(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, updated_user: UserCreate):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        return None
    for var, value in vars(updated_user).items():
        setattr(db_user, var, value)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()
