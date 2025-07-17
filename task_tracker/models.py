from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func

# database model
class Task(db.Model): 
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    task: Mapped[str] = mapped_column(String(200))
    date_created: Mapped[datetime] = mapped_column(
    server_default=func.now()
    )

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="tasks")

    def __repr__(self) -> str:
        return f"Task(id={self.id!r}, task={self.task!r}, date_created={self.date_created!r})"
    


class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True)
    password_hash: Mapped[str] = mapped_column(String(128))

    todos: Mapped[List["Task"]] = relationship(back_populates="user")


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"