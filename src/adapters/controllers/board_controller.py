from typing import List
from src.core.use_cases.create_board import CreateBoardUseCase
from src.core.use_cases.delete_board import DeleteBoardUseCase
from src.core.use_cases.rename_board import RenameBoardUseCase
from src.core.use_cases.list_user_boards import ListUserBoardsUseCase
from src.core.use_cases.list_board_tasks import ListBoardTasksUseCase
from src.core.use_cases.list_board_statuses import ListBoardStatusesUseCase
from src.adapters.schemas.board import BoardCreate, BoardResponse, BoardUpdate
from src.adapters.schemas.task import TaskResponse
from src.adapters.schemas.status import StatusResponse
from src.core.entities.board import Board


class BoardController:
    def __init__(
        self,
        create_board_use_case: CreateBoardUseCase,
        delete_board_use_case: DeleteBoardUseCase,
        rename_board_use_case: RenameBoardUseCase,
        list_user_boards_use_case: ListUserBoardsUseCase,
        list_board_tasks_use_case: ListBoardTasksUseCase,
        list_board_statuses_use_case: ListBoardStatusesUseCase,
    ):
        self.create_board_use_case = create_board_use_case
        self.delete_board_use_case = delete_board_use_case
        self.rename_board_use_case = rename_board_use_case
        self.list_user_boards_use_case = list_user_boards_use_case
        self.list_board_tasks_use_case = list_board_tasks_use_case
        self.list_board_statuses_use_case = list_board_statuses_use_case

    def create_board(self, board_data: BoardCreate) -> BoardResponse:
        board = Board(name=board_data.name, user_id=board_data.user_id)
        created_board = self.create_board_use_case.execute(board)
        return BoardResponse(
            id=created_board.id,
            name=created_board.name,
            user_id=created_board.user_id,
        )

    def delete_board(self, board_id: int) -> None:
        return self.delete_board_use_case.execute(board_id)

    def rename_board(self, board_data: BoardUpdate) -> BoardResponse:
        updated_board = self.rename_board_use_case.execute(
            board_data.id, board_data.name
        )
        return BoardResponse(
            id=updated_board.id,
            name=updated_board.name,
            user_id=updated_board.user_id,
        )

    def list_user_boards(self, user_id: int) -> List[BoardResponse]:
        boards = self.list_user_boards_use_case.execute(user_id)
        return list(
            map(
                lambda board: BoardResponse(
                    id=board.id,
                    name=board.name,
                    user_id=board.user_id,
                ),
                boards,
            )
        )

    def list_board_tasks(self, board_id: int) -> List[TaskResponse]:
        tasks = self.list_board_tasks_use_case.execute(board_id)
        return [
            TaskResponse(
                id=task.id,
                title=task.title,
                description=task.description,
                start=task.start,
                end=task.end,
                user_id=task.user_id,
                status_id=task.status_id,
                board_id=task.board_id,
            )
            for task in tasks
        ]

    def list_board_statuses(self, board_id: int) -> List[StatusResponse]:
        statuses = self.list_board_statuses_use_case.execute(board_id)
        return [
            StatusResponse(
                id=status.id,
                name=status.name,
                user_id=status.user_id,
                board_id=status.board_id,
            )
            for status in statuses
        ]
