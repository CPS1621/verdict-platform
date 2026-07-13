from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from app.database.database import Base


class VerdictEvent(Base):
    __tablename__ = "verdict_events"

    id = Column(Integer, primary_key=True, index=True)


    rule_id = Column(Integer, nullable=False)

    rule_name = Column(String(200), nullable=False)

    verdict = Column(String(50), nullable=False)

    event_data = Column(Text, nullable=False)

    verdict_hash = Column(String(64), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)