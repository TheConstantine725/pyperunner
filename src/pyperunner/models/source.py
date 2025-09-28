from dataclasses import dataclass
from typing import Optional, List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from pyperunner.models import SourceBase


class Table(SourceBase):
    __tablename__ = "src_tables"

    id: Mapped[int] = mapped_column(primary_key=True)
    table_alias: Mapped[str] = mapped_column(unique=True)
    raw_query: Mapped[str] 
    dbapi_dialect: Mapped[str]
    dbapi_driver: Mapped[str]
    is_incrementally_loaded: Mapped[bool]

    merge_keys: Mapped[List["MergeKeys"]] = relationship("MergeKeys", back_populates="table", cascade="all, delete-orphan")
    source_schema: Mapped[List["Schema"]] = relationship("Schema", back_populates="table", cascade= "all, delete-orphan")

class Schema(SourceBase):
    __tablename__ = "src_schema"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    table_id: Mapped[int] = mapped_column(ForeignKey("src_tables.id"))
    field_name: Mapped[str] = mapped_column(index=True)
    type_code: Mapped[int]
    display_size: Mapped[Optional[int]]
    internal_size: Mapped[Optional[int]]
    precision: Mapped[Optional[int]]
    scale: Mapped[Optional[int]]
    null_ok: Mapped[Optional[bool]]
    
    table: Mapped["Table"] = relationship("Table", back_populates="source_schema")
    

class MergeKeys(SourceBase):
    __tablename__ = "src_merge_keys"
    
    merge_key_idx: Mapped[int] = mapped_column( index = True, primary_key=True)
    column_name: Mapped[str]
    table_id: Mapped[int] = mapped_column(ForeignKey("src_tables.id"))

    table: Mapped["Table"] = relationship("Table", back_populates="merge_keys")
    

class TypeMaps(SourceBase):
    __tablename__ = "tm_type_maps"
    
    id: Mapped[int] =  mapped_column(primary_key=True, index=True)
    dbapi_driver: Mapped[str]
    source_type_code: Mapped[int]
    norm_dtype: Mapped[str]