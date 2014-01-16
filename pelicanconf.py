#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'James Nicholson'
SITENAME = u'nicholsonjf.com'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

GITHUB_USER = 'nicholsonjf'
GITHUB_SKIP_FORK = True

STATIC_PATHS = ['images', 'files', 'extra/robots.txt', 'extra/favicon.ico']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# Blogroll
LINKS = None

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/nicholsonjf'),
          ('linkedin', 'http://www.linkedin.com/in/nicholsonjf'),
          ('github', 'http://github.com/nicholsonjf'),)

DEFAULT_PAGINATION = 5

TAG_CLOUD_MAX_ITEMS = 10

DISPLAY_CATEGORIES_ON_MENU = False

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'nl2br']
THEME = os.path.join(os.environ.get('HOME'),
                     'projects/pelican-bootstrap3')

BOOTSTRAP_THEME = 'readable'

USE_OPEN_GRAPH = True
#OPEN_GRAPH_FB_APP_ID = '202018593182706'
#OPEN_GRAPH_IMAGE = 'images/dandydev.png'

PLUGIN_PATH = os.path.join(os.environ.get('HOME'),
                           'projects/tools/pelican-plugins')

DISQUS_SITENAME = 'nicholsonjf'
#ADDTHIS_PROFILE = 'ra-520d4af6518bf3c7'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
