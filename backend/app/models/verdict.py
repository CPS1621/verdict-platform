from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text,
    Boolean,
)
from sqlalchemy.sql import func

from app.database.database import Base


class Verdict(Base):
    __tablename__ = "verdict_events"

    id = Column(Integer, primary_key=True, index=True)

    rule_id = Column(Integer, nullable=False)

    rule_name = Column(String, nullable=False)

    verdict = Column(String, nullable=False)

    event_data = Column(Text, nullable=False)

    verdict_hash = Column(String(64), nullable=False)

    is_superseded = Column(
        Boolean,
        default=False,
        nullable=False
    )

    superseded_by = Column(
        Integer,
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )