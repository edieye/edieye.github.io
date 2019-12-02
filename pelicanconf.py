#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Author
AUTHOR = 'Edie Ye'
AUTHOR_BIO = 'Formerly a child. Currently a software developer. Aspiring to be a lottery winner.'
SITEURL = 'http://edieye.ca'
PATH = 'content'
#READERS = {'html': None}

# Basic
TIMEZONE = 'America/Vancouver'
DEFAULT_LANG = 'en'
THEME = './themes/pelican-svbtle'
GOOGLE_ANALYTICS = 'UA-153651252-1'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URLs
PAGE_URL = 'about/'

# LINKS
LINKS = (('about', '/pages/about.html'),
         ('mail', 'mailto:edie_ye@hotmail.com'),
         ('github', 'https://github.com/edieye'),
         ('linkedin','http://www.linkedin.com/in/edie-ye'),
         ('instagram', 'http://www.instagram.com/edieyee')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
