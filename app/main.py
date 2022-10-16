import typing

import fastapi
from fastapi.middleware import cors

from app import db, deps, events, models

app = fastapi.FastAPI()

app.add_middleware(
    cors.CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", events.create_start_app_handler(app))  # type: ignore


@app.get("/")
def get_all_vequest(
    _: fastapi.Request,
    db: db.Database = fastapi.Depends(deps.get_db_client),
) -> typing.Any:
    return {"verification_requests": db.get_all_unapproved()}


@app.put("/{pubkey}")
def update_vequest(
    pubkey: str,
    verification_request: models.VerificationRequests,
    db: db.Database = fastapi.Depends(deps.get_db_client),
) -> typing.Any:
    return db.update(pubkey, verification_request)
