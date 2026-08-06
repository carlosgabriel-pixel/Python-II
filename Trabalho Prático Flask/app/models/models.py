from datetime import datetime
from typing import Optional, List
from sqlalchemy import ForeignKey, String, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin
from app import db, login

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(128))
    foto: Mapped[Optional[str]] = mapped_column(String(256))
    bio: Mapped[Optional[str]] = mapped_column(Text)
    last_login: Mapped[Optional[datetime]] = mapped_column(DateTime, default=datetime.now)

    # Relacionamento 1-N com Post
    posts: Mapped[List['Post']] = relationship(back_populates='author', cascade='all, delete-orphan')

class Post(db.Model):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str] = mapped_column(Text)
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    # Relacionamento N-1 com User
    author: Mapped[User] = relationship(back_populates='posts')

@login.user_loader
def load_user(id: str):
    return db.session.get(User, int(id))