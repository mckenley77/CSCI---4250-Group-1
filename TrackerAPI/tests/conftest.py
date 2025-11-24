import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ---------------------------------------------------------------------
# Make sure Python can import main.py and db_models.py from TrackerAPI
# ---------------------------------------------------------------------
# This file lives in TrackerAPI/tests/conftest.py
# So parents[1] == TrackerAPI directory
TRACKERAPI_DIR = Path(__file__).resolve().parents[1]

if str(TRACKERAPI_DIR) not in sys.path:
    sys.path.insert(0, str(TRACKERAPI_DIR))

import main          # now this imports TrackerAPI/main.py
from db_models import Base  # imports TrackerAPI/db_models.py

# ---------------------------------------------------------------------
# Test database setup (in-memory SQLite)
# ---------------------------------------------------------------------

TEST_SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    TEST_SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

TestingSessionLocal = sessionmaker(bind=engine)


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def db_session():
    """
    Create a fresh DB session for each test and
    override the session inside main.py
    """
    connection = engine.connect()
    transaction = connection.begin()

    session = TestingSessionLocal(bind=connection)
    main.session = session  # override the global session in main.py

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(db_session):
    """
    Provides a FastAPI testing client
    """
    with TestClient(main.app) as c:
        yield c
