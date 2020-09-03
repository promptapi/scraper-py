# pylint: disable=C0103
import sys

from scraper import Scraper

if __name__ == '__main__':

    url = 'https://pypi.org/classifiers1/'
    scraper = Scraper(url)
    response = scraper.get()

    if response.get('error', None):
        sys.stdout.write(f'response: {response}\n')
    else:
        result = response['result']
        status = response['status']

        sys.stdout.write(f'result.keys(): {result.keys()}\n')
        sys.stdout.write(f'headers: {result["headers"]}\n')
        sys.stdout.write(f'status: {status}\n')

        save_result = scraper.save('/tmp/foo.html')  # noqa: S108
        sys.stdout.write(f'save_result: {save_result}\n')
