import sqlmodel
from sqlalchemy import engine

from app import models


class Database:
    db_engine: engine.Engine

    def __init__(self, database_url: str) -> None:
        self.db_engine = sqlmodel.create_engine(database_url, echo=False)

    def get_all_unapproved(self) -> list[models.VerificationRequests]:
        """Get all row from the verification_requests table

        Returns:
            list[models.VerificationRequests]: list of all verification requests.
        """
        with sqlmodel.Session(self.db_engine) as session:
            return session.exec(
                sqlmodel.select(models.VerificationRequests)  # type: ignore
            ).all()

    def update(
        self, pubkey: str, verification_request: models.VerificationRequests
    ) -> models.VerificationRequests | None:
        """Update the verification request

        Args:
            pubkey (str): public key of the verification request
            verification_request (models.VerificationRequests): the new verification request

        Returns:
            models.VerificationRequests: the updated verification request
        """
        print(pubkey, type(pubkey))
        with sqlmodel.Session(self.db_engine) as session:
            statement = sqlmodel.select(  # type: ignore
                models.VerificationRequests
            ).where(models.VerificationRequests.pubkey == pubkey)
            result = session.exec(statement).one()

            # This results in an sqlalchemy.orm.exc.UnmappedInstanceError:
            # result.copy(update=verification_request.dict(exclude_unset=True))

            result.pubkey = verification_request.pubkey
            result.info_link = verification_request.info_link
            result.official_website = verification_request.official_website
            result.official_email = verification_request.official_email
            result.organization_id = verification_request.organization_id
            result.approved = verification_request.approved

            session.add(result)
            session.commit()

            return session.get(models.VerificationRequests, verification_request.pubkey)
