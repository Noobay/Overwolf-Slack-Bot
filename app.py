#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import environ as env
from sys import argv

import urllib2
from urllib2 import HTTPError

import bottle
from bottle import default_app, request, route, response, get, post

import re

docsUrl = 'http://developers.overwolf.com/documentation/'
searchUrlBase = docsUrl + 'search/'
searchUrl = ''

@get('/')
def index():
    response.content_type = 'text/plain; charset=utf-8'
    ret = 'Hello'
    return ret


@get('/docs/')
@post('/docs/')
def docs():
    args = request.body.read()

    reArgs = re.search('(?<=text=).+?(?=&)', args)

    if reArgs is None:
        return docsUrl

    textArgs = reArgs.group(0)

    buildsearchurl(textArgs.split('+'))

    try:
        response = urllib2.urlopen(searchUrl)     
    except HTTPError:
        return 'your search term: "' + textArgs.replace('+',' ') + '" was not found in overwolf\'s documentation'
     
    return response.geturl();

def buildsearchurl(searchArgs):
    global searchUrl

    searchUrl = searchUrlBase

    for counter, argument in enumerate(searchArgs):
        print searchUrl
        searchUrl += argument
        if counter < len(searchArgs)-1:
            searchUrl += '-'

bottle.run(host='0.0.0.0', port=argv[1])
