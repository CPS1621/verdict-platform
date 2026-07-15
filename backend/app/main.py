from fastapi import FastAPI

from app.database.database import engine
from app.database.base import Base

from app.api.users import router as user_router
from app.api.rules import router as rule_router
from app.api.verdicts import router as verdict_router
from app.api.dashboard import router as dashboard_router
from app.api.validator import router as validator_router

app = FastAPI(
    title="CyBreach Validator API"
)

# Create all database tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(user_router)
app.include_router(rule_router)
app.include_router(verdict_router)
app.include_router(dashboard_router)
app.include_router(validator_router)

@app.get("/")
def root():
    return {"message": "Backend is working"}


@app.get("/health")
def health():
    return {"status": "ok"}