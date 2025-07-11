from typing import Any, Dict, Optional, List
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.core.repository_interfaces.status_repository import IStatusRepository
from src.core.entities.status import Status
from src.infrastructure.persistence.models.status import Status as StatusModel


class StatusRepository(IStatusRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, status: Status) -> Status:
        status_db = StatusModel(
            name=status.name,
            user_id=status.user_id,
            board_id=status.board_id,
        )
        self.session.add(status_db)
        self.session.commit()
        self.session.refresh(status_db)
        return Status(
            id=status_db.id,
            name=status_db.name,
            user_id=status_db.user_id,
            board_id=status_db.board_id,
        )

    def find_by_id(self, id: int) -> Optional[Status]:
        status_db = self.session.get(StatusModel, id)
        return Status(
            id=status_db.id,
            name=status_db.name,
            user_id=status_db.user_id,
            board_id=status_db.board_id,
        ) if status_db else None

    def list_all(self) -> List[Status]:
        status_db = self.session.scalars(select(StatusModel)).all()
        return list(map(lambda status: Status(
            id=status.id,
            name=status.name,
            user_id=status.user_id,
            board_id=status.board_id,
        ), status_db))

    def delete(self, id: int) -> None:
        status_db = self.session.get(StatusModel, id)
        self.session.delete(status_db)
        self.session.commit()

    def filter_by(self, filter_dict: Dict[str, Any]) -> List[Status]:
        status_db = self.session.scalars(select(StatusModel).filter_by(**filter_dict)).all()
        return list(map(lambda status: Status(
            id=status.id,
            name=status.name,
            user_id=status.user_id,
            board_id=status.board_id,
        ), status_db))
