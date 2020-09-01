# pylint: disable=R0201,E1101

import os
# import sys
import unittest

from scraper import Scraper

# from collections import namedtuple


EXISTING_PROMPTAPI_TOKEN = os.environ.get('PROMPTAPI_TOKEN', None)


class TestSimple(unittest.TestCase):
    def test_api_token(self):
        scraper = Scraper()
        scraper.get(dict(foo=1), 22)
        self.assertTrue(scraper)


if __name__ == '__main__':
    unittest.main()
