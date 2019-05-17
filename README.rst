==============
pytest-chalice
==============

.. image:: https://img.shields.io/pypi/v/pytest-chalice.svg
    :target: https://pypi.org/project/pytest-chalice
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-chalice.svg
    :target: https://pypi.org/project/pytest-chalice
    :alt: Python versions

.. image:: https://travis-ci.org/studio3104/pytest-chalice.svg?branch=master
    :target: https://travis-ci.org/studio3104/pytest-chalice
    :alt: See Build Status on Travis CI

A set of py.test fixtures for AWS Chalice

----

Features
------------

- Launch the local gateway per test function
- Provide an abstracted client fixture to access the local gateway
- Expose an interface to overwrite response context with arbitrary objects
    - As of Chalice version 1.8.0, LocalGateway object doesn't handle Cognito's context
    - Not only for this purpose, it's an interface provided to allow custom contexts in unit tests


Requirements
------------

- `pytest`_
- `Chalice`_


Installation
------------

You can install "pytest-chalice" via `pip`_ from `PyPI`_::

    $ pip install pytest-chalice


Usage
-----

.. code-block:: python

    from chalice import Chalice

    app = Chalice(__name__)


    @app.route('/')
    def index:
        return {'hello': 'world'}


.. code-block:: python

    from http import HTTPStatus


    def test_index(client):
        response = client.get('/')
        assert response.status_code == HTTPStatus.OK
        assert response.json == {'hello': 'world'}


See `examples <https://github.com/studio3104/pytest-chalice/tree/master/examples>`_ for more detailed

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-chalice" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/studio3104/pytest-chalice/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
.. _`Chalice`: https://github.com/aws/chalice
