from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from pyperunner.models import SourceBase


class Tables(SourceBase):
    __tablename__ = "src_tables"

    id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement="auto",)
    table_alias: Mapped[str] = mapped_column(unique=True)
    # query_fk: Mapped[int] = mapped_column(ForeignKey("query.id"))
    is_incremental_load: Mapped[bool]

    # queries: Mapped["Query"] = relationship(back_populates="src_tables")
    # merge_keys: Mapped["MergeKeys"] = relationship(back_populates="src_tables")

    
class Query(SourceBase):
    __tablename__ = "src_queries"

    id: Mapped[Optional[int]] = mapped_column( primary_key=True, autoincrement="auto")
    table_id: Mapped[int] = mapped_column(ForeignKey("src_tables.id"))
    raw_query: Mapped[str] 
    has_bind_params: Mapped[bool]
    
    # tables: Mapped["Tables"] = relationship(back_populates="src_queries")


class MergeKeys(SourceBase):
    __tablename__ = "src_merge_keys"
    
    table_id: Mapped[int] = mapped_column(ForeignKey("src_tables.id"), primary_key=True)
    id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement="auto")
    column_name: Mapped[str]

    # tables: Mapped["Tables"] = relationship(back_populates="src_merge_keys")


    