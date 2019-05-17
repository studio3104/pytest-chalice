import pytest

from chalice import Chalice

from app import app as chalice_app


@pytest.fixture
def app() -> Chalice:
    return chalice_app
