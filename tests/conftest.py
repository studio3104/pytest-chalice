# -*- coding: utf-8 -*-

from typing import Any, Dict, Iterator, Union

import pytest

from chalice import Chalice

pytest_plugins = 'pytester'


@pytest.fixture
def app():
    # type: () -> Iterator[Union[Iterator, Iterator[Chalice]]]
    app = Chalice(__name__)

    @app.route('/', methods=('GET', 'HEAD', 'POST', 'OPTIONS', 'PUT', 'DELETE', 'TRACE', 'PATCH', 'LINK', 'UNLINK'))
    def index():
        # type: () -> Dict[str, str]
        return {'hello': 'world'}

    @app.route('/context')
    def context():
        # type: () -> Dict[str, Dict[str, Any]]
        context = app.current_request.context
        return {'context': context}

    @app.route('/string')
    def string():
        # type: () -> str
        return 'Foo'

    yield app
