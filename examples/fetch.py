# pylint: disable=C0103

from scraper import Scraper


def fetch_via_get(url):
    scraper = Scraper(url)
    return scraper.get()


if __name__ == '__main__':
    response = fetch_via_get('https://pypi.org/classifiers/')
    result = response['result']
    status = response['status']

    print(result.keys())  # noqa: T001
    print(status)  # noqa: T001
