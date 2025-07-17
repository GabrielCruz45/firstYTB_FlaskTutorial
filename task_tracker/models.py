from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import func

# database model
class Todo(db.Model): # change 'Todo' to 'Task'
    __tablename__ = 'todos'

    id: Mapped[int] = mapped_column(primary_key=True)
    task: Mapped[str] = mapped_column(String(200))
    date_created: Mapped[datetime.datetime] = mapped_column(
    server_default=func.now()
    )

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="todos")

    def __repr__(self) -> str:
        return f"Todo(id={self.id!r}, task={self.task!r}, datetime={self.date_created!r})"
    


class User(db.Model):
    __tablename__ = 'users'
    # __bind_key__ = 'users' # check for change on __init__.py

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True)
    password_hash: Mapped[str] = mapped_column(String(128))

    todos: Mapped[List["Todo"]] = relationship(back_populates="user")


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"