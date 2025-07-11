from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from src.core.entities.board import Board
from src.core.entities.task import Task
from src.core.entities.status import Status


class IBoardRepository(ABC):
    @abstractmethod
    def save(self, board: Board) -> Board:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Board]:
        pass

    @abstractmethod
    def list_all(self) -> List[Board]:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass

    @abstractmethod
    def filter_by(self, filter_dict: Dict[str, Any]) -> List[Board]:
        pass

    @abstractmethod
    def update(self, id: int, data: Dict[str, Any]) -> Board:
        pass

    @abstractmethod
    def list_tasks(self, board_id: int) -> List[Task]:
        pass

    @abstractmethod
    def list_statuses(self, board_id: int) -> List[Status]:
        pass
