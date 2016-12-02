#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import environ as env
from sys import argv

import bottle
from bottle import default_app, request, route, response, get
global urlList 
urlList = ""

@get('/')
def index():
    response.content_type = 'text/plain; charset=utf-8'
    return ret
def onInit():
    global urlList

    
    f = open('urllist.txt', 'r')
    urlString = f.read()
    urlList = urlList.split('\n');
    
onInit()
bottle.run(host='0.0.0.0', port=argv[1])
