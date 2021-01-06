try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Haunted Castle (C) Game, Nov 2017',
    'author': 'Spyros Dellas',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'spyrosdellas@yahoo.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['haunted_castle'],
    'scripts': ['bin\starting.py'],
    'name': 'Haunted Castle'
}

setup(**config)
