from src.core.repository_interfaces.user_repository import IUserRepository
from src.core.repository_interfaces.status_repository import IStatusRepository
from src.core.repository_interfaces.board_repository import IBoardRepository
from src.core.entities.status import Status
from src.core.use_cases.exceptions import UserNotFoundError, BoardNotFoundError


class CreateStatusUseCase:
    def __init__(
        self,
        status_repository: IStatusRepository,
        user_repository: IUserRepository,
        board_repository: IBoardRepository,
    ):
        self.user_repository = user_repository
        self.status_repository = status_repository
        self.board_repository = board_repository

    def execute(self, status: Status) -> Status:
        user_exist = self.user_repository.find_by_id(status.user_id)
        if not user_exist:
            raise UserNotFoundError("User not found")
        board_exist = self.board_repository.find_by_id(status.board_id)
        if not board_exist:
            raise BoardNotFoundError("Board not found")
        return self.status_repository.save(status)
