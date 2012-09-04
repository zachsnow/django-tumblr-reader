from setuptools import setup
from tumblr_reader import __version__

setup(
    name='django-tumblr-reader',
    version=__version__,
    author='Zach Snow',
    author_email='z@zachsnow.com',
    packages=['tumblr_reader', 'tumblr_reader.templatetags'],
    url='http://zachsnow.com/projects/',
    license='LICENSE.rst',
    description=r"""django-tumblr-reader is a simple, reusable Django application that defines template tags for embedding your Tumblr blog in your Django website.""",
    long_description=open('README.rst').read(),
)
