import typing

import fastapi

from app import db, deps, events

app = fastapi.FastAPI()

app.add_event_handler("startup", events.create_start_app_handler(app))  # type: ignore


@app.get("/")
def get_all_vequest(
    _: fastapi.Request,
    db: db.Database = fastapi.Depends(deps.get_db_client),
) -> typing.Any:
    return {"verification_requests": db.get_all_unapproved()}
