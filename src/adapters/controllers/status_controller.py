from typing import List
from src.core.use_cases.create_status import CreateStatusUseCase
from src.core.use_cases.delete_status import DeleteStatusUseCase
from src.core.use_cases.list_user_status import ListUserStatusUseCase
from src.adapters.schemas.status import StatusCreate, StatusResponse
from src.core.entities.status import Status


class StatusController:
    def __init__(
        self,
        create_status_use_case: CreateStatusUseCase,
        delete_status_use_case: DeleteStatusUseCase,
        list_user_status_use_case: ListUserStatusUseCase,
    ):
        self.create_status_use_case = create_status_use_case
        self.delete_status_use_case = delete_status_use_case
        self.list_user_status_use_case = list_user_status_use_case

    def create_status(self, status_data: StatusCreate) -> StatusResponse:
        status = Status(
            name=status_data.name,
            user_id=status_data.user_id,
            board_id=status_data.board_id,
        )
        created_status = self.create_status_use_case.execute(status)
        return StatusResponse(
            id=created_status.id,
            name=created_status.name,
            user_id=created_status.user_id,
            board_id=created_status.board_id,
        )

    def delete_status(self, status_id: int) -> None:
        return self.delete_status_use_case.execute(status_id)
    
    def list_user_status(self, user_id: int) -> List[StatusResponse]:
        statuses = self.list_user_status_use_case.execute(user_id)
        return list(
            map(
                lambda status: StatusResponse(
                    id=status.id,
                    name=status.name,
                    user_id=status.user_id,
                    board_id=status.board_id,
                ),
                statuses,
            )
        )
