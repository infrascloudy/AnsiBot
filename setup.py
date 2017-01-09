from setuptools import setup, find_packages

setup(
    install_requires=['nltk',
                      'geoip2',
                      'git+https://github.com/CloudBotIRC/mcstatus.git@master',
                      'microdata',
                      'sqlalchemy',
                      'watchdog',
                      'lxml',
                      'beautifulsoup4',
                      'feedparser',
                      'requests',
                      'psutil',
                      'requests-oauthlib',
                      'tweepy',
                      'pyenchant',
                      'pythonwhois',
                      'imgurpython',
                      'isodate'],
    packages=find_packages(exclude=['test'])
)
