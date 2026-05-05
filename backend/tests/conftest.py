import pytest
from app import create_app
from app.core.database import db
from app.core.redis import r

@pytest.fixture
def app():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })

    with app.app_context():
        # Set up testing schema
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()
        db.engine.dispose()
        r.flushdb()

@pytest.fixture
def client(app):
    return app.test_client()
