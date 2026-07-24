from app.database.database import Base

# Import all models so SQLAlchemy registers them
from app.models.user import User
from app.models.rule import Rule
from app.models.verdict import Verdict