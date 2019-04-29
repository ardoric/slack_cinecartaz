#!/usr/bin/python

import pyslack
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
import cinecartaz
import json

slack_info = json.load(open('/home/ardoric/.slack'))


slack = pyslack.SlackClient(slack_info['access_key'])

estreias = cinecartaz.estreias()

message = '*' + estreias['title'] + '*\n'
for filme in estreias['filmes']:
    message += '<' + filme['url'] +  '|' + filme['title'] + '>'
    if filme.has_key('original_title') and filme['title'] != filme['original_title']:
       message += ' - ' + filme['original_title']
    message += '\n'

# slack.chat_post_message('@ardoric', message, username='moviebot', icon_url='https://dl.dropboxusercontent.com/u/15116829/moviebot.jpg')
slack.chat_post_message('#movie-night', message, username='moviebot', icon_url='https://dl.dropboxusercontent.com/u/15116829/moviebot.jpg')

