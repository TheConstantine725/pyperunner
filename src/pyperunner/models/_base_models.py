from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData
from pydantic import BaseModel


class SourceBase(DeclarativeBase):
    # metadata = MetaData(schema="source")
    ...

class Validator(BaseModel):
    ...