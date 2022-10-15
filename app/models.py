import pydantic
import sqlmodel
from sqlalchemy import orm

pydantic.BaseConfig.arbitrary_types_allowed = True


class VerificationRequest(sqlmodel.SQLModel, table=True):
    pubkey: str | None = sqlmodel.Field(default=None, primary_key=True)  # type: ignore
    info_link: pydantic.HttpUrl | None = sqlmodel.Field(default=None)  # type: ignore
    official_website: pydantic.HttpUrl | None = sqlmodel.Field(default=None)  # type: ignore
    official_email: pydantic.EmailStr = sqlmodel.Field(default_factory=None)  # type: ignore
    organization_id: str | None = sqlmodel.Field(default=None)  # type: ignore
    approved: bool = sqlmodel.Field(default=False)  # type: ignore

    @classmethod
    @orm.declared_attr
    def __tablename__(cls):
        return "verification_requests"
