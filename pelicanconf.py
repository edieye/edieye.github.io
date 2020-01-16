#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Author
AUTHOR = 'EDIE YE'
AUTHOR_BIO = 'Software developer from Vancouver, BC.'
SITENAME = 'Just For Fun'
SITEURL = 'edieye.ca'
#SITEURL = 'http://localhost:8000'
PATH = 'content'

# Basic
TIMEZONE = 'America/Vancouver'
DEFAULT_LANG = 'en'
THEME = './themes/pelican-svbtle'
GOOGLE_ANALYTICS = 'UA-153651252-1'
DISQUS_SITENAME = 'edieye-ca'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# STATIC PATHS
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

PAGE_URL = 'about/'

# LINKS
LINKS = (('about', '/pages/about.html'),
         ('mail', 'mailto:edie_ye@hotmail.com'),
         ('github', 'https://github.com/edieye'),
         ('linkedin','https://www.linkedin.com/in/edie-ye'),
         ('instagram', 'https://www.instagram.com/edieyee')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
