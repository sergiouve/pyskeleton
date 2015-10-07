try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'New project',
    'author': 'Sergio Uve',
    'url': 'http://new-project.com',
    'download_url': 'hhtp://new-project.com/download',
    'author_email': 'sergiouve@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'project_name'
}

setup(**config)
