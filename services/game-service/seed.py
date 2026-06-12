import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app.database import SessionLocal, engine
from app.models import Base, Games

GAMES = [
    {"title": "The Legend of Zelda: Breath of the Wild", "genre": "Action-Adventure", "platform": "Nintendo Switch", "release_year": 2017, "cover_url": None},
    {"title": "Red Dead Redemption 2",                   "genre": "Action-Adventure", "platform": "PlayStation 4",  "release_year": 2018, "cover_url": None},
    {"title": "Elden Ring",                              "genre": "RPG",              "platform": "PC",             "release_year": 2022, "cover_url": None},
    {"title": "Hades",                                   "genre": "Roguelike",        "platform": "PC",             "release_year": 2020, "cover_url": None},
    {"title": "God of War",                              "genre": "Action-Adventure", "platform": "PlayStation 4",  "release_year": 2018, "cover_url": None},
]


def run():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    imported = 0
    for data in GAMES:
        existing = db.query(Games).filter(Games.title == data["title"]).first()
        if existing:
            continue
        game = Games(**data)
        db.add(game)
        imported += 1

    db.commit()
    db.close()
    print(f"Imported {imported} games.")


if __name__ == "__main__":
    run()
