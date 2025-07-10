class ApplicationError(Exception):
    pass

class UserAlreadyExistsError(ApplicationError):
    pass

class UserNotFoundError(ApplicationError):
    pass

class StatusNotFoundError(ApplicationError):
    pass

class TaskNotFoundError(ApplicationError):
    pass

class InvalidCredentialsError(ApplicationError):
    pass
