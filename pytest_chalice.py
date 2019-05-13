# -*- coding: utf-8 -*-

import pytest

import json
import re

from chalice.config import Config
from chalice.local import LocalGateway


class InternalLocalGateway(LocalGateway):
    def __init__(self, *args, **kwargs):
        self.custom_context = {}
        super(InternalLocalGateway, self).__init__(*args, **kwargs)

    def _generate_lambda_event(self, *args, **kwargs):
        event = super(InternalLocalGateway, self)._generate_lambda_event(*args, **kwargs)
        event['requestContext'].update(self.custom_context)
        return event


UPPERCASE_PATTERN = re.compile('([A-Z])')


class ResponseHandler:
    def __init__(self, values):
        self.values = {}

        for key, value in values.items():
            snake_key = re.sub(UPPERCASE_PATTERN, lambda x: '_' + x.group(1).lower(), key)
            self.values[snake_key] = value

        try:
            self.values['json'] = json.loads(self.values['body'])
        except json.JSONDecodeError:
            pass

    def __getattr__(self, key):
        try:
            return self.values[key]
        except KeyError:
            raise AttributeError("'{}' object has no attribute '{}'".format(self.__class__.__name__, key))


class RequestHandler(object):
    METHODS = ('get', 'head', 'post', 'options', 'put', 'delete', 'trace', 'patch', 'link', 'unlink')

    def __init__(self, app):
        self.local_gateway = InternalLocalGateway(app, Config())

    @property
    def custom_context(self):
        return self.local_gateway.custom_context

    @custom_context.setter
    def custom_context(self, context):
        self.local_gateway.custom_context = context

    def __getattr__(self, method):
        if method not in self.METHODS:
            raise AttributeError("'{}' object has no attribute '{}'".format(self.__class__.__name__, method))

        def request(path, headers={}, body=''):
            response = self.local_gateway.handle_request(method=method.upper(), path=path, headers=headers, body=body)
            return ResponseHandler(response)

        return request


@pytest.fixture
def client(app):
    yield RequestHandler(app)
