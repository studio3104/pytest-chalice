from typing import Dict

from chalice import Chalice

app = Chalice(app_name='simple')


@app.route('/')
def index() -> Dict[str, str]:
    return {'hello': 'world'}
