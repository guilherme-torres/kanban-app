from src.core.repository_interfaces.board_repository import IBoardRepository
from src.core.entities.board import Board
from src.core.use_cases.exceptions import BoardNotFoundError, BoardAlreadyExistsError


class RenameBoardUseCase:
    def __init__(self, board_repository: IBoardRepository):
        self.board_repository = board_repository

    def execute(self, board_id: int, board_name: str) -> Board:
        board_exist = self.board_repository.find_by_id(board_id)
        if not board_exist:
            raise BoardNotFoundError("Board not found")
        duplicated_name = self.board_repository.filter_by({"name": board_name})
        if duplicated_name:
            raise BoardAlreadyExistsError("Board already exists")
        return self.board_repository.update(board_id, {"name": board_name})
