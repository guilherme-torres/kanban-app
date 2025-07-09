from src.core.repository_interfaces.status_repository import IStatusRepository
from src.core.use_cases.exceptions import StatusNotFoundError


class DeleteStatusUseCase:
    def __init__(self, status_repository: IStatusRepository):
        self.status_repository = status_repository

    def execute(self, status_id: int) -> None:
        status_exist = self.status_repository.find_by_id(status_id)
        if not status_exist:
            raise StatusNotFoundError("Status not found")
        return self.status_repository.delete(status_id)
