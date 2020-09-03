![Python](https://img.shields.io/badge/python-3.7.4-green.svg)
![Version](https://img.shields.io/badge/version-0.1.1-orange.svg)
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
from scraper import Scraper

url = 'https://pypi.org/classifiers/'
scraper = Scraper(url)
response = scraper.get()

if response.get('error', None):
    # response['error']  returns error message
    # response['status'] returns http status code
    # {'error': 'Not Found', 'status': 404}
    print(response)
else:
    result = response['result']
    
    print(result['headers'])   # returns response headers 
    print(result['data'])      # returns fetched html
    print(result['url'])       # returns fetched url
    print(response['status'])  # returns http status code

    save_result = scraper.save('/tmp/my-html.html')  # save to file
    if save_result.get('error', None):
        # we have save error
        pass
    else:
        print(save_result)    # contains saved file path and file size
        # {'file': '/tmp/my-html.html', 'size': 321322}
```

---

## TODO

- Add `xpath` extractor.

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
