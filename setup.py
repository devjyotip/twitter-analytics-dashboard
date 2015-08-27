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
        "mongoengine-0.8.7",
	"pymongo-2.8.1",
        "nltk",
        'numpy',
        'gevent',
        'gevent-socketio',
        'flask',
        'argcomplete'
    ],
)
