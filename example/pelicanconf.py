# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Fundor333'
SITENAME = 'Pelican e perchè generare siti statici'
SITEURL = ''
PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'it'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# =======================================
# Theme config


THEME = 'theme/pelican-blue'

SOCIAL = (
          ('github', 'https://github.com/fundor333'),
          ('twitter', 'https://twitter.com/fundor333'),
          )

DEFAULT_PAGINATION = 10

SIDEBAR_DIGEST = 'Sito di prova per il Pycon'

FAVICON = 'url-to-favicon'

DISPLAY_PAGES_ON_MENU = True
TWITTER_USERNAME = 'Fundor333'


MENUITEMS = (('Blog', SITEURL),)

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# ===========================================
# Plugins

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']
