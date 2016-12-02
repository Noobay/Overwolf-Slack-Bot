#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import environ as env
from sys import argv

import urllib2
from urllib2 import HTTPError

import bottle
from bottle import default_app, request, route, response, get

searchUrlBase = 'http://developers.overwolf.com/documentation/search/'
searchUrl = ''

bottle.debug(True)

@get('/')
def index():
    response.content_type = 'text/plain; charset=utf-8'
    ret = 'Hello'
    return ret

@route('/docs/<args>')
def docs(args):

    buildsearchurl(args.split(' '))

    try:
        response = urllib2.urlopen(searchUrl)     
    except HTTPError:
        return 'your search term: "' + args.replace('%',' ') +  '" was not found in the OverWolf documentations'
     
    return response.geturl();

def buildsearchurl(searchargs):
    global searchUrl

    searchUrl = searchUrlBase

    for counter, argument in enumerate(searchargs):
        print searchUrl
        searchUrl += argument
        if counter < len(searchargs)-1:
            searchUrl += '-'

bottle.run(host='0.0.0.0', port=argv[1])
