# -*- coding: utf-8 -*-

import pytest

from .plugins import RequestHandler


@pytest.fixture
def client(app):
    yield RequestHandler(app)
