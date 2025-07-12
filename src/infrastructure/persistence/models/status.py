from typing import List
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.infrastructure.persistence.database.db import Base


class Status(Base):
    __tablename__ = "status"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    board_id: Mapped[int] = mapped_column(ForeignKey("boards.id"))

    user: Mapped["User"] = relationship(back_populates="status")
    board: Mapped["Board"] = relationship(back_populates="status")
    tasks: Mapped[List["Task"]] = relationship(
        back_populates="status", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Status(id={self.id}, name={self.name}, user_id={self.user_id})"
