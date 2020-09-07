# pylint: disable=R0201

import json
import os
import re
from http import HTTPStatus

import requests

__all__ = ['Scraper']

REQUIRED_PARAMS = []
VALID_METHODS = ['GET', 'POST']
VALID_PARAMS = [
    'auth_password',
    'auth_username',
    'cookie',
    'country',
    'referer',
    'selector',
]
PROMPTAPI_ENDPOINT = os.environ.get(
    'PROMPTAPI_TEST_ENDPOINT', 'https://api.promptapi.com/scraper'
)
URL_PATTERN = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$',
    re.IGNORECASE,
)


class Scraper:
    def __init__(self, url, timeout=10):
        self.url = url
        self.timeout = timeout
        self.apikey = None
        self.data = None

    def _validate(self, params):
        apikey = os.environ.get('PROMPTAPI_TOKEN', None)
        if not apikey:
            return (
                dict(error='You need to set PROMPTAPI_TOKEN environment variable'),
                None,
            )
        self.apikey = apikey

        valid_params = dict()
        for param in params.keys():
            if param in VALID_PARAMS:
                valid_params[param] = params.get(param)

        for required_param in REQUIRED_PARAMS:
            if required_param not in valid_params:
                return dict(error=f'{required_param} param is required'), None

        return dict(), valid_params

    def _http(self, method, params=None, body=None):
        params.update(url=self.url)
        if body is None:
            body = dict()
        headers = dict(apikey=self.apikey)
        http_error = None
        try:
            response = requests.request(
                method,
                PROMPTAPI_ENDPOINT,
                timeout=self.timeout,
                params=params,
                headers=headers,
                data=body,
            )
            response.raise_for_status()
        except requests.exceptions.Timeout:
            return dict(
                error='Connection timeout error',
                status=response.status_code,
            )
        except requests.exceptions.TooManyRedirects:
            return dict(
                error='Too many redirects error',
                status=response.status_code,
            )
        except requests.exceptions.ConnectionError:
            return dict(
                error='Connection error',
                status=response.status_code,
            )
        except requests.exceptions.HTTPError as err:
            http_error = dict(
                error=str(err),
                status=response.status_code,
            )
        try:
            result = response.json()
        except json.decoder.JSONDecodeError as err:
            return dict(
                error=f'JSON decoding error: {str(err)}',
                status=response.status_code,
            )

        if http_error:
            return dict(
                error=result.get('message', http_error),
                status=response.status_code,
            )

        if response.status_code != HTTPStatus.OK.value:
            return dict(
                error=result.get('message', response.reason),
                status=response.status_code,
            )
        return dict(result=result, status=response.status_code)

    def get(self, params=None, timeout=5):
        if params is None:
            params = dict()
        if not isinstance(params, dict):
            return dict(
                error='Type error, you need to pass dict',
                status=None,
            )
        validation_result, valid_params = self._validate(params)
        if validation_result.get('error', None):
            return validation_result
        self.timeout = timeout
        response = self._http('GET', valid_params)

        if response.get('result', None) and response.get('result').get('data', None):
            self.data = response['result']['data']

        if response.get('result', None) and response.get('result').get(
            'data-selector', None
        ):
            self.data = response['result']['data-selector']
            response['result']['data'] = self.data
        return response

    def save(self, filename):
        if not self.data:
            return dict(error='Data is not available')

        save_extension = '.html'
        save_data = self.data
        if isinstance(self.data, list):
            save_extension = '.json'
            save_data = json.dumps(self.data)

        file_basename, _ = os.path.splitext(filename)
        file_savename = f'{file_basename}{save_extension}'
        save_file = os.path.abspath(file_savename)
        try:
            with open(save_file, 'w') as fp:
                fp.write(save_data)
        except TypeError:
            return dict(error='Incorrect data to save...')
        except FileNotFoundError:
            return dict(error=f'File not found: {save_file}')
        return dict(file=save_file, size=os.stat(save_file).st_size)
