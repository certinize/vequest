from starlette import requests as requests_

from app import db


def get_db_client(request: requests_.Request) -> db.Database:
    return request.app.state.db
