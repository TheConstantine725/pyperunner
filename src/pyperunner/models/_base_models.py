from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData
from pydantic import BaseModel


class SourceBase(DeclarativeBase):
    ...

class Validator(BaseModel):
    ...