# pylint: disable=C0103
import sys

from scraper import Scraper

if __name__ == '__main__':

    url = 'https://pypi.org/classifiers/'
    scraper = Scraper(url)

    fetch_params = dict(country='EE')
    # valid params:
    # auth_password
    # auth_username
    # cookie
    # country
    # referer'
    response = scraper.get(params=fetch_params)

    if response.get('error', None):
        sys.stdout.write(f'response: {response}\n')
    else:
        result = response['result']
        status = response['status']

        sys.stdout.write(f'result.keys(): {result.keys()}\n')
        sys.stdout.write(f'headers: {result["headers"]}\n')
        sys.stdout.write(f'status: {status}\n')

        save_result = scraper.save('/tmp/my-html.html')  # noqa: S108
        if save_result.get('error', None):
            # we have error!
            pass
        else:
            # save completed!
            pass
        sys.stdout.write(f'save_result: {save_result}\n')
