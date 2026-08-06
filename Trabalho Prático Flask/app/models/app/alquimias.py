from datetime import datetime
from app import db
from app.models.models import User, Post

def validate_user_password(username, password):
    user = db.session.query(User).filter_by(username=username).first()
    if user and user.password == password:
        return user
    return None

def user_exists(username):
    user = db.session.query(User).filter_by(username=username).first()
    return user

def create_user(username, password, foto=None, bio=None, remember=False, last_login=None):
    new_user = User(
        username=username,
        password=password,
        foto=foto,
        bio=bio,
        last_login=last_login or datetime.now()
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

def create_post(body, user):
    new_post = Post(body=body, author=user, timestamp=datetime.now())
    db.session.add(new_post)
    db.session.commit()
    return new_post

def get_timeline():
    return db.session.query(Post).order_by(Post.timestamp.desc()).limit(5).all()