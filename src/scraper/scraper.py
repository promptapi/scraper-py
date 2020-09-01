# pylint: disable=R0201

import os

# import requests
from console import console

__all__ = ['Scraper']

console = console(source=__name__)

REQUIRED_PARAMS = ['url']
VALID_PARAMS = ['url', 'auth_password', 'auth_username', 'cookie', 'country', 'referer']


class Scraper:
    def __init__(self, *args, **kwargs):
        self.timeout = 1
        super().__init__(*args, **kwargs)

    def _http(self, method, params):
        console('method', method)
        console('self.timeout', self.timeout)

        apikey = os.environ.get('PROMPTAPI_TOKEN', None)
        if not apikey:
            return dict(error='You need to set PROMPTAPI_TOKEN environment variable')

        for param in params.keys():
            console('param', param)

        # result = dict()
        # headers = dict(apikey=apikey)
        # http_error = None
        return dict(ok=True)

    def get(self, params, timeout=5):
        self.timeout = timeout
        result = self._http('GET', params)
        console(result)
