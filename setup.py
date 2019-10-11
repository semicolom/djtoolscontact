import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-tools-contact',
    version='1.3.2',
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    description='A simple Django app to manage company contact information.',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Toni Colom',
    author_email='toni@semicolom.com',
    install_requires=[
        'django-recaptcha',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
