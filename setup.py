import pathlib

from setuptools import find_packages, setup

CURRENT_WORKING_DIRECTORY = pathlib.Path(__file__).parent.resolve()
LONG_DESCRIPTION = (CURRENT_WORKING_DIRECTORY / 'README.md').read_text(encoding='utf-8')

setup(
    name='pa-scraper',
    version='0.2.2',
    description="Python wrapper for Prompt API's Scraper API",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/promptapi/scraper-py',
    author='Prompt API',
    author_email='hello@promptapi.com',
    license='MIT',
    python_requires='>=3.7',
    package_dir={'': 'src'},
    packages=find_packages(where='src', exclude=['tests', 'examples']),
    extras_require={
        'development': ['vb-console'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Text Processing :: General',
    ],
    keywords='promptapi, scrape, extract, parse, download',
    install_requires=['requests'],
    project_urls={
        'Prompt API': 'https://promptapi.com',
        'Scraper API': 'https://promptapi.com/marketplace/description/scraper-api',
        'Source': 'https://github.com/promptapi/scraper-py',
    },
)
