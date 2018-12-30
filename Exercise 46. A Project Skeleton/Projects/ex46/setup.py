try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'An example for Exercise 46',
    'author': 'Alejandro Camara',
    'url': 'https://github.com/AlejandroCamara/Learn_Python_3_the_Hard_Way',
    'download_url': 'https://github.com/AlejandroCamara/Learn_Python_3_the_Hard_Way',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex46'],
    'scripts': [],
    'name': 'ex46'
}

setup(**config)