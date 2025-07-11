from typing import List
from src.core.repository_interfaces.user_repository import IUserRepository
from src.core.repository_interfaces.board_repository import IBoardRepository
from src.core.entities.board import Board
from src.core.use_cases.exceptions import UserNotFoundError, ApplicationError


class ListUserBoardsUseCase:
    def __init__(
        self,
        user_repository: IUserRepository,
        board_repository: IBoardRepository,
    ):
        self.user_repository = user_repository
        self.board_repository = board_repository

    def execute(self, user_id: int) -> List[Board]:
        if not user_id:
            raise ApplicationError("user_id required")
        user_exist = self.user_repository.find_by_id(user_id)
        if not user_exist:
            raise UserNotFoundError("User not found")
        return self.board_repository.filter_by({"user_id": user_id})
