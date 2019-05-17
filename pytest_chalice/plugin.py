# -*- coding: utf-8 -*-

from _pytest.config import Config

from .fixtures import client  # noqa


def pytest_configure(config):
    # type: (Config) -> None
    config.addinivalue_line(
        'markers',
        'app: A Chalice application object',
    )
