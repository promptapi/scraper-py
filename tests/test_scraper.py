# pylint: disable=R0201,E1101

import os
import unittest

from scraper import Scraper

EXISTING_PROMPTAPI_TOKEN = os.environ.get('PROMPTAPI_TOKEN', None)


class TestSimple(unittest.TestCase):
    def test_api_token(self):
        os.environ['PROMPTAPI_TOKEN'] = ''  # noqa: S105

        scraper = Scraper('https://fake.com/')
        response = scraper.get()
        self.assertTrue(response.get('error', None))

        response = scraper.get(params='foo')
        self.assertTrue(response.get('error', None))


if __name__ == '__main__':
    unittest.main()
