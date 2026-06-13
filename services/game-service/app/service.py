# Application layer — business logic.
#
# Calls repository functions and returns Pydantic schemas (not raw ORM objects).
# Raises ValueError when a game is not found — routes.py turns it into a 404.
#
# Implement these four functions:
# - add_game(db, data) -> GameOut
# - fetch_game(db, game_id) -> GameOut        (raises ValueError if not found)
# - fetch_all_games(db, limit, offset) -> GameList
# - find_games(db, q, limit, offset) -> GameList   (delegates to search_games in repository)


from sqlalchemy.orm import Session
from app import repository
from app.schemas import GameCreate, GameOut, GameList
from app.infrastructure.cache import set_game_summary


def add_game(db: Session, data: GameCreate) -> GameOut:
    game = repository.create_game(db, data)
    result = GameOut.model_validate(game)
    try:
        set_game_summary(
            result.id,
            {
                "id": result.id,
                "title": result.title,
                "genre": result.genre,
                "platform": result.platform,
                "cover_url": result.cover_url,
            },
        )
    except Exception as e:
        # Log the error but don't fail the request if Redis is down
        print(f"Warning: failed to cache game summary for {result.id}: {e}")
    return result


def fetch_game(db: Session, game_id: str) -> GameOut:
    game = repository.get_game(db, game_id)
    if game is None:
        raise ValueError(f"Game {game_id} not found")
    return GameOut.model_validate(game)


def fetch_all_games(db: Session, limit: int = 20, offset: int = 0) -> GameList:
    games, total = repository.list_games(db, limit=limit, offset=offset)
    return GameList(
        items=[GameOut.model_validate(g) for g in games],
        total=total,
        limit=limit,
        offset=offset,
    )


def find_games(db: Session, q: str, limit: int = 20, offset: int = 0) -> GameList:
    games, total = repository.search_games(db, q, limit=limit, offset=offset)
    return GameList(
        items=[GameOut.model_validate(g) for g in games],
        total=total,
        limit=limit,
        offset=offset,
    )


def remove_game(db: Session, game_id: str) -> None:
    if not repository.delete_game(db, game_id):
        raise ValueError(f"Game {game_id} not found")