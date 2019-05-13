# -*- coding: utf-8 -*-

import pytest

from .handlers import RequestHandler


@pytest.fixture
def client(app):
    yield RequestHandler(app)
