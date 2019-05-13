# -*- coding: utf-8 -*-

import pytest


class TestRequest:
    @pytest.mark.parametrize('method',  (
        'get', 'head', 'post', 'put', 'delete', 'trace', 'patch', 'link', 'unlink',
    ))
    def test_json_response(self, method, client):
        response = getattr(client, method)('/')
        assert response.status_code == 200
        assert response.json == {'hello': 'world'}

    def test_invalid_method(self, client):
        with pytest.raises(AttributeError, match=r' object has no attribute '):
            client.invalid_method('/')

    def test_string_response_dont_have_json_attribute(self, client):
        response = client.get('/string')
        assert not hasattr(response, 'json')


class TestCustomContext:
    def test_check_default_context(self, client):
        response = client.get('/context')
        assert response.json == {
            'context': {
                'httpMethod': 'GET',
                'identity': {'sourceIp': '127.0.0.1'},
                'path': '/context',
                'resourcePath': '/context',
            }
        }

    def test_custom_context(self, client):
        client.custom_context = {
            'authorizer': {'claims': {}},
        }

        response = client.get('/context')
        response_context = response.json['context']
        assert 'httpMethod' in response_context
        assert 'identity' in response_context
        assert 'path' in response_context
        assert 'resourcePath' in response_context
        assert 'authorizer' in response_context
