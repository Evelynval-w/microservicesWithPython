# Interface layer — HTTP endpoints.
#
# Define a router with prefix="/v1/games" and implement these endpoints:
# - POST   /v1/games/          -> create a game (201)
# - GET    /v1/games/          -> list games (limit/offset pagination)
# - GET    /v1/games/search    -> search games by title (?q=...)
# - GET    /v1/games/{game_id} -> get one game by ID (404 if not found)
#
# IMPORTANT: declare /search BEFORE /{game_id} in your router.
# If /{game_id} comes first, FastAPI will try to match "search" as an ID
# and return a 422 Unprocessable Entity error.

# Interface layer — HTTP endpoints.

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import service, schemas
from app.security import require_admin
from app.infrastructure.cache import get_game_summary


router = APIRouter(prefix="/v1/games", tags=["games"])


@router.post("/", response_model=schemas.GameOut, status_code=201)
def create_game(data: schemas.GameCreate, db: Session = Depends(get_db)):
    return service.add_game(db, data)


@router.get("/", response_model=schemas.GameList)
def list_games(limit: int = 20, offset: int = 0, db: Session = Depends(get_db)):
    return service.fetch_all_games(db, limit=limit, offset=offset)


@router.get("/search", response_model=schemas.GameList)
def search_games(q: str, limit: int = 20, offset: int = 0, db: Session = Depends(get_db)):
    return service.find_games(db, q, limit=limit, offset=offset)


@router.get("/{game_id}", response_model=schemas.GameOut)
def get_game(game_id: str, db: Session = Depends(get_db)):
    try:
        return service.fetch_game(db, game_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{game_id}/summary")
def game_summary(game_id: str):
    data = get_game_summary(game_id)
    if data is None:
        raise HTTPException(status_code=404, detail="No summary cached")
    return data


@router.delete("/{game_id}", dependencies=[Depends(require_admin)])
def delete_game(game_id: str, db: Session = Depends(get_db)):
    try:
        service.remove_game(db, game_id)
        return {"deleted": True, "id": game_id}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))