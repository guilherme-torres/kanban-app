from typing import Optional
from datetime import datetime
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.infrastructure.persistence.database.db import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    start: Mapped[Optional[datetime]]
    end: Mapped[Optional[datetime]]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    status_id: Mapped[int] = mapped_column(ForeignKey("status.id"))
    board_id: Mapped[int] = mapped_column(ForeignKey("boards.id"))

    user: Mapped["User"] = relationship(back_populates="tasks")
    status: Mapped["Status"] = relationship(back_populates="tasks")
    board: Mapped["Board"] = relationship(back_populates="tasks")

    def __repr__(self):
        return (
            f"Task(id={self.id}, title={self.title}, description={self.description},"
            f"start={self.start}, end={self.end}, user_id={self.user_id}, status_id={self.status_id})"
        )
