from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.adapters.controllers.board_controller import BoardController
from src.core.use_cases.create_board import CreateBoardUseCase
from src.core.use_cases.delete_board import DeleteBoardUseCase
from src.core.use_cases.list_user_boards import ListUserBoardsUseCase
from src.core.use_cases.rename_board import RenameBoardUseCase
from src.core.use_cases.exceptions import UserNotFoundError, BoardAlreadyExistsError, BoardNotFoundError
from src.infrastructure.persistence.repositories.board_repository import BoardRepository
from src.infrastructure.persistence.repositories.user_repository import UserRepository
from src.infrastructure.persistence.database.db import get_db_session
from src.adapters.schemas.board import BoardCreate, BoardResponse, BoardUpdate


router = APIRouter(prefix="/boards")

def get_board_controller(db: Session):
    user_repository = UserRepository(db)
    board_repository = BoardRepository(db)
    create_board_use_case = CreateBoardUseCase(
        board_repository=board_repository,
        user_repository=user_repository
    )
    delete_board_use_case = DeleteBoardUseCase(board_repository)
    list_user_boards_use_case = ListUserBoardsUseCase(
        board_repository=board_repository,
        user_repository=user_repository
    )
    rename_board_use_case = RenameBoardUseCase(board_repository)
    return BoardController(
        create_board_use_case=create_board_use_case,
        delete_board_use_case=delete_board_use_case,
        rename_board_use_case=rename_board_use_case,
        list_user_boards_use_case=list_user_boards_use_case,
    )

@router.post("/", response_model=BoardResponse)
def create_board(board_data: BoardCreate, db: Session = Depends(get_db_session)):
    try:
        board_controller = get_board_controller(db)
        return board_controller.create_board(board_data)
    except UserNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    except BoardAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Board already exists"
        )

@router.delete("/{id}") 
def delete_board(id: int, db: Session = Depends(get_db_session)):
    try:
        board_controller = get_board_controller(db)
        return board_controller.delete_board(id)
    except BoardNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Board not found"
        )
    
@router.post("/{id}", response_model=BoardResponse)
def rename_board(id: int, board_data: BoardUpdate, db: Session = Depends(get_db_session)):
    try:
        board_controller = get_board_controller(db)
        return board_controller.rename_board(board_data)
    except BoardNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Board not found"
        )
    except BoardAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Board already exists"
        )
    
@router.get("/", response_model=List[BoardResponse])
def list_user_boards(user_id: int, db: Session = Depends(get_db_session)):
    try:
        board_controller = get_board_controller(db)
        return board_controller.list_user_boards(user_id)
    except UserNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
