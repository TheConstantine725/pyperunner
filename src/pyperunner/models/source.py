from dataclasses import dataclass
from typing import Optional, List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from pyperunner.models import SourceBase


class Table(SourceBase):
    __tablename__ = "src_tables"

    id: Mapped[int] = mapped_column(primary_key=True)
    table_alias: Mapped[str] = mapped_column(unique=True)
    is_incremental_load: Mapped[bool]
    raw_query: Mapped[str] 

    merge_keys: Mapped[List["MergeKeys"]] = relationship("MergeKeys", back_populates="table", cascade="all, delete-orphan")

# class BindParams(SourceBase):
#     __tablename__ = "src_bind_params"
    
#     table_id: Mapped[int] = mapped_column("source_table_id", ForeignKey("src_tables.id"), primary_key=True)
#     table_bind_params_idx: Mapped[int] = mapped_column("bind_param_idx", index=True, primary_key=True)
#     column_name: Mapped[str]


class MergeKeys(SourceBase):
    __tablename__ = "src_merge_keys"
    
    merge_key_idx: Mapped[int] = mapped_column( index=True, nullable=False)
    column_name: Mapped[str]
    table_id: Mapped[int] = mapped_column(ForeignKey("src_tables.id"))

    table: Mapped["Table"] = relationship("Table", back_populates="merge_keys")
    



    