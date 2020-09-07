![Python](https://img.shields.io/badge/python-3.7.4-green.svg)
![Version](https://img.shields.io/badge/version-0.2.2-orange.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Build Status](https://travis-ci.org/promptapi/scraper-py.svg?branch=main)](https://travis-ci.org/promptapi/scraper-py)

# Prompt API - Scraper API - Python Package

`pa-scraper` is a python wrapper for [scraper api][scraper-api] with few
more extra cream and sugar.

## Requirements

1. You need to signup for [Prompt API][promptapi-signup]
1. You need to subscribe [scraper api][scraper-api], test drive is **free!!!**
1. You need to set `PROMPTAPI_TOKEN` environment variable after subscription.

then;

```bash
$ pip install pa-scraper
```

---

## Example Usage

Examples can be found [here][examples].

```python
# examples/fetch.py

from scraper import Scraper

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

```

You can add url parameters for extra operations. Valid parameters are:

- `auth_password`: for HTTP Realm auth password
- `auth_username`: for HTTP Realm auth username
- `cookie`: URL Encoded cookie header.
- `country`: 2 character country code. If you wish to scrape from an IP address of a specific country.
- `referer`: HTTP referer header
- `selector`: CSS style selector path such as `a.btn div li`. If `selector`
  is enabled, returning result will be collection of data and saved file
  will be in `.json` format.

Here is an example with using url parameters and `selector`:

```python
# examples/fetch_with_params.py

from scraper import Scraper

url = 'https://pypi.org/classifiers/'
scraper = Scraper(url)

fetch_params = dict(country='EE', selector='ul li button[data-clipboard-text]')
response = scraper.get(params=fetch_params)

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
    # we have an array...

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

```

Default **timeout** value is set to `10` seconds. You can change this while
initializing the instance:

```python
scraper = Scraper(url, timeout=50)  # 50 seconds timeout...
```

---

## License

This project is licensed under MIT

---

## Contributer(s)

* [Prompt API](https://github.com/promptapi) - Creator, maintainer

---

## Contribute

All PR’s are welcome!

1. `fork` (https://github.com/promptapi/scraper-py/fork)
1. Create your `branch` (`git checkout -b my-feature`)
1. `commit` yours (`git commit -am 'Add awesome features...'`)
1. `push` your `branch` (`git push origin my-feature`)
1. Than create a new **Pull Request**!

This project is intended to be a safe,
welcoming space for collaboration, and contributors are expected to adhere to
the [code of conduct][coc].

---

[scraper-api]:      https://promptapi.com/marketplace/description/scraper-api
[promptapi-signup]: https://promptapi.com/#signup-form
[coc]:              https://github.com/promptapi/scraper-py/blob/main/CODE_OF_CONDUCT.md
[examples]:         https://github.com/promptapi/scraper-py/blob/main/examples/
