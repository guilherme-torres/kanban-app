from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from src.core.entities.task import Task


class ITaskRepository(ABC):
    @abstractmethod
    def save(self, task: Task) -> Task:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Task]:
        pass

    @abstractmethod
    def list_all(self) -> List[Task]:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass

    @abstractmethod
    def update(self, id: int, data: Dict[str, Any]) -> Task:
        pass

    @abstractmethod
    def filter_by(self, filter_dict: Dict[str, Any]) -> List[Task]:
        pass
