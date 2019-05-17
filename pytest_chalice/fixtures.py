# -*- coding: utf-8 -*-

from typing import Iterator

import pytest

from chalice import Chalice

from .handlers import RequestHandler


@pytest.fixture
def client(app):
    # type: (Chalice) -> Iterator[Chalice]
    yield RequestHandler(app)
