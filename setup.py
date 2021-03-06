from setuptools import setup, find_packages

setup(
    name='smm',
    version='0.1',
    packages=['smm'],
    url='https://github.com/devjyotip/twitter-analytics-dashboard',
    description='Real-Time, Twitter sentiment analyzer dashboard',
    install_requires=[
        "requests",
        "requests_oauthlib",
        "nltk",
        'numpy',
        'gevent',
        'gevent-socketio',
        'flask',
        'argcomplete'
    ],
)
