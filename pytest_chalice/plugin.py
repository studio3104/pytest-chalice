# -*- coding: utf-8 -*-

from .fixtures import client  # noqa


def pytest_configure(config):
    config.addinivalue_line(
        'markers',
        'app: A Chalice application object',
    )
