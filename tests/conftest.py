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

    @app.route('/context')
    def context():
        context = app.current_request.context
        return {'context': context}

    @app.route('/string')
    def string():
        return 'Foo'

    yield app
