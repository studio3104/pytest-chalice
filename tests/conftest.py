# -*- coding: utf-8 -*-

import pytest

from chalice import Chalice

pytest_plugins = 'pytester'


@pytest.fixture
def app():
    app = Chalice(__name__)

    @app.route('/', methods=('GET', 'HEAD', 'POST', 'OPTIONS', 'PUT', 'DELETE', 'TRACE', 'PATCH', 'LINK', 'UNLINK'))
    def index():
        return {'hello': 'world'}

    yield app
