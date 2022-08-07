import pytest

from app.main import app


@pytest.fixture()
def test_client():
    return app.test_client()
