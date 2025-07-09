from src.core.use_cases.create_status import CreateStatusUseCase
from src.core.use_cases.delete_status import DeleteStatusUseCase
from src.adapters.schemas.status import StatusCreate, StatusResponse
from src.core.entities.status import Status


class StatusController:
    def __init__(
        self,
        create_status_use_case: CreateStatusUseCase,
        delete_status_use_case: DeleteStatusUseCase,
    ):
        self.create_status_use_case = create_status_use_case
        self.delete_status_use_case = delete_status_use_case

    def create_status(self, status_data: StatusCreate) -> StatusResponse:
        status = Status(
            name=status_data.name,
            user_id=status_data.user_id,
        )
        created_status = self.create_status_use_case.execute(status)
        return StatusResponse(
            id=created_status.id,
            name=created_status.name,
            user_id=created_status.user_id,
        )

    def delete_status(self, status_id: int) -> None:
        return self.delete_status_use_case.execute(status_id)
