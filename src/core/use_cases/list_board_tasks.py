from typing import List
from src.core.repository_interfaces.board_repository import IBoardRepository
from src.core.entities.task import Task
from src.core.use_cases.exceptions import BoardNotFoundError


class ListBoardTasksUseCase:
    def __init__(self, board_repository: IBoardRepository):
        self.board_repository = board_repository

    def execute(self, board_id: int) -> List[Task]:
        board_exist = self.board_repository.find_by_id(board_id)
        if not board_exist:
            raise BoardNotFoundError("Board not found")
        return self.board_repository.list_tasks(board_id)
