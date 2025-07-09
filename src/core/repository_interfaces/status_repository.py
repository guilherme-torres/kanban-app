from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from src.core.entities.status import Status


class IStatusRepository(ABC):
    @abstractmethod
    def save(self, status: Status) -> Status:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Status]:
        pass

    @abstractmethod
    def list_all(self) -> List[Status]:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass

    @abstractmethod
    def filter_by(self, filter_dict: Dict[str, Any]) -> List[Status]:
        pass
