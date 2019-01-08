try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Exercise 49. Making Sentences',
    'author': 'Alejandro Camara',
    'url': 'https://github.com/AlejandroCamara/Learn_Python_3_the_Hard_Way',
    'download_url': 'https://github.com/AlejandroCamara/Learn_Python_3_the_Hard_Way',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex49'],
    'scripts': [],
    'name': 'ex49'
}

setup(**config)