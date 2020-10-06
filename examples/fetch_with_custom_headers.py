# pylint: disable=C0103
from scraper import Scraper

if __name__ == '__main__':

    url = 'https://pypi.org/classifiers/'
    scraper = Scraper(url)

    fetch_params = dict(country='EE', selector='ul li button[data-clipboard-text]')
    custom_headers = {
        'X-Referer': 'https://www.google.com',
        'X-User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
    }
    timeout = 30
    response = scraper.get(params=fetch_params, headers=custom_headers, timeout=timeout)

    if response.get('error', None):
        # response['error']  returns error message
        # response['status'] returns http status code

        # Example: {'error': 'Not Found', 'status': 404}
        print(response)  # noqa: T001
    else:
        data = response['result']['data']
        headers = response['result']['headers']
        url = response['result']['url']
        status = response['status']

        # print(data)  # noqa: T001
        # ['<button class="button button--small margin-top margin-bottom copy-tooltip copy-tooltip-w" ...\n', ]

        print(len(data))  # noqa: T001
        # 734

        print(headers)  # noqa: T001
        # {'Content-Length': '321322', 'Content-Type': 'text/html; charset=UTF-8', ... }

        print(status)  # noqa: T001
        # 200

        save_result = scraper.save('/tmp/my-data.json')  # noqa: S108
        if save_result.get('error', None):
            # save error occured...
            # add you code here...
            pass
        print(save_result)  # noqa: T001
        # {'file': '/tmp/my-data.json', 'size': 174449}
