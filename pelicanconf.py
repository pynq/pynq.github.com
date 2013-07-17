#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'PyNQ'
SITENAME = u'PyNQ.org'
SITEURL = ''
SITESUBTITLE = "Official home of the Python North Queensland Users Group."
THEME = 'notmyidea'

DISQUS_SITENAME = 'pynq'
GOOGLE_ANALYTICS = 'UA-42534285-1'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social widget
SOCIAL = (('Mailing list', 'https://groups.google.com/d/forum/pynq?hl=en'),
          ('GitHub', 'https://github.com/pynq/pynq.github.com'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PAGE_DIR = 'pages'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-.*'
NEWEST_FIRST_ARCHIVES = True

STATIC_PATHS = ['images', 'files', 'extras/CNAME', 'extras/favicon.ico', 'extras/.nojekyll']
EXTRA_PATH_METADATA = {
    'extras/CNAME': {'path': 'CNAME'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/.nojekyll': {'path': '.nojekyll'}
}
#All files in the `extras` directory get picked up.
#directory='content/extras'
#STATIC_PATHS.extend([(os.path.join('extras', filename), filename) for filename in os.listdir(directory)])
EXTRA_TEMPLATES_PATHS = ['templates']


TYPOGRIFY = True
TIMEZONE = 'Australia/Queensland'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

#Save all pages exactly as they are recorded in their slug
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}'

