import sqlmodel
from sqlalchemy import engine

from app import models


class Database:
    db_engine: engine.Engine

    def __init__(self, database_url: str) -> None:
        self.db_engine = sqlmodel.create_engine(database_url, echo=True)

    def get_all_unapproved(self) -> list[models.VerificationRequest]:
        """Get all row from the verification_requests table

        Returns:
            list[models.VerificationRequest]: list of all verification requests.
        """
        with sqlmodel.Session(self.db_engine) as session:
            return session.exec(
                sqlmodel.select(models.VerificationRequest)  # type: ignore
            ).all()
