from src.core.repository_interfaces.board_repository import IBoardRepository
from src.core.repository_interfaces.user_repository import IUserRepository
from src.core.entities.board import Board
from src.core.use_cases.exceptions import BoardAlreadyExistsError, UserNotFoundError


class CreateBoardUseCase:
    def __init__(
        self,
        board_repository: IBoardRepository,
        user_repository: IUserRepository,
    ):
        self.board_repository = board_repository
        self.user_repository = user_repository
        
    def execute(self, board: Board) -> Board:
        board_exist = self.board_repository.filter_by({"name": board.name})
        if board_exist:
            raise BoardAlreadyExistsError("Board already exists")
        user_exist = self.user_repository.find_by_id(board.user_id)
        if not user_exist:
            raise UserNotFoundError("User not found")
        return self.board_repository.save(board)
