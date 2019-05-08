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
