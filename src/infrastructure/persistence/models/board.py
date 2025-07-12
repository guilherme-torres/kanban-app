from typing import List
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.infrastructure.persistence.database.db import Base


class Board(Base):
    __tablename__ = "boards"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="boards")
    tasks: Mapped[List["Task"]] = relationship(
        back_populates="board", cascade="all, delete-orphan"
    )
    status: Mapped[List["Status"]] = relationship(
        back_populates="board", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Board(id={self.id}, name={self.name}, user_id={self.user_id})"
