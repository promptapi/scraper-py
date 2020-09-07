# pylint: disable=C0103
from scraper import Scraper

if __name__ == '__main__':

    url = 'https://pypi.org/classifiers/'
    scraper = Scraper(url)
    response = scraper.get()

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

        # print(data) # print fetched html, will be long :)

        print(headers)  # noqa: T001
        # {'Content-Length': '321322', 'Content-Type': 'text/html; charset=UTF-8', ... }

        print(status)  # noqa: T001
        # 200

        save_result = scraper.save('/tmp/my-data.html')  # noqa: S108

        if save_result.get('error', None):
            # save error occured...
            # add you code here...
            pass

        print(save_result)  # noqa: T001
        # {'file': '/tmp/my-data.html', 'size': 321322}
