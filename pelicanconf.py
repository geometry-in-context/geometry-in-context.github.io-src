#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Joseph Thomas'
SITENAME = u'Geometry in Context'
SITEURL = ''

THEME = './subtle'

PATH = 'content'

TIMEZONE = 'America/Phoenix'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

INDEX_SAVE_AS = 'blog_index.html'

SOCIAL = False
LINKS = False
RESPONSIVE_IMAGES = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

JST_SITE_ROOT = "http://geometry-in-context.github.io/"
MENUITEMS = [('About', JST_SITE_ROOT), 
             ('Links/Contact', JST_SITE_ROOT + 'pages/linkscontact.html'), 
             ('Transformations', JST_SITE_ROOT + 'pages/transformations.html'),
             ('Trigonometry', JST_SITE_ROOT + 'pages/trigonometry.html'),
             ('Volume', JST_SITE_ROOT + 'pages/volume.html')]

# PAGE_URL = '../{slug}.html'
# PAGE_SAVE_AS = '../{slug}.html'

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = [ 'render_math', 'better_figures_and_images', 'pelican_vimeo' ]

STATIC_PATHS = ['images','downloads']
