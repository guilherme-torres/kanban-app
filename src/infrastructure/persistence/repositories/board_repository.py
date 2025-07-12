from typing import List, Optional, Dict, Any
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.core.entities.board import Board
from src.core.entities.task import Task
from src.core.entities.status import Status
from src.core.repository_interfaces.board_repository import IBoardRepository
from src.infrastructure.persistence.models.board import Board as BoardModel


class BoardRepository(IBoardRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, board: Board) -> Board:
        board_db = BoardModel(name=board.name, user_id=board.user_id)
        self.session.add(board_db)
        self.session.commit()
        self.session.refresh(board_db)
        return Board(id=board_db.id, name=board_db.name, user_id=board_db.user_id)

    def find_by_id(self, id: int) -> Optional[Board]:
        board_db = self.session.get(BoardModel, id)
        return (
            Board(id=board_db.id, name=board_db.name, user_id=board_db.user_id)
            if board_db
            else None
        )

    def list_all(self) -> List[Board]:
        board_db = self.session.scalars(select(BoardModel)).all()
        return list(
            map(
                lambda board: Board(
                    id=board.id, name=board.name, user_id=board.user_id
                ),
                board_db,
            )
        )

    def delete(self, id: int) -> None:
        board_db = self.session.get(BoardModel, id)
        self.session.delete(board_db)
        self.session.commit()

    def filter_by(self, filter_dict: Dict[str, Any]) -> List[Board]:
        board_db = self.session.scalars(
            select(BoardModel).filter_by(**filter_dict)
        ).all()
        return list(
            map(
                lambda board: Board(
                    id=board.id,
                    name=board.name,
                    user_id=board.user_id,
                ),
                board_db,
            )
        )

    def update(self, id: int, data: Dict[str, Any]) -> Board:
        board_db = self.session.get(BoardModel, id)
        for key, value in data.items():
            setattr(board_db, key, value)
        self.session.commit()
        self.session.refresh(board_db)
        return Board(id=board_db.id, name=board_db.name, user_id=board_db.user_id)

    def list_tasks(self, board_id: int) -> List[Task]:
        board_db = self.session.get(BoardModel, board_id)
        return [
            Task(
                id=task_db.id,
                title=task_db.title,
                description=task_db.description,
                start=task_db.start,
                end=task_db.end,
                user_id=task_db.user_id,
                status_id=task_db.status_id,
                board_id=task_db.board_id,
            )
            for task_db in board_db.tasks
        ]

    def list_statuses(self, board_id: int) -> List[Status]:
        board_db = self.session.get(BoardModel, board_id)
        return [
            Status(
                id=status_db.id,
                name=status_db.name,
                user_id=status_db.user_id,
                board_id=status_db.board_id,
            )
            for status_db in board_db.status
        ]
