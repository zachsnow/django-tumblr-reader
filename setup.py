from setuptools import setup
from tumblr_reader import __version__

setup(
    name='Django Tumblr Reader',
    version=__version__,
    author='Zach Snow',
    author_email='z@zachsnow.com',
    packages=['tumblr_reader'],
    url='http://zachsnow.com/projects/',
    license='LICENSE.rst',
    description=r"""Django Tumblr Reader is a simple, reusable Django application that defines template tags for embedding your Tumblr blog in your Django website.""",
    long_description=open('README.rst').read(),
)
