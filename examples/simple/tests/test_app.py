from http import HTTPStatus
from pytest_chalice.handlers import RequestHandler


def test_index(client: RequestHandler) -> None:
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json == {'hello': 'world'}
