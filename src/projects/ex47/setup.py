try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'LPTHW Exercise 47 - Unit tests',
    'author': 'Spyros Dellas',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'spyrosdellas@yahoo.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'Exercise 47'
}

setup(**config)
