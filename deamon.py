#!/usr/bin/python

import ari

# Change your Asterisk access details here
url = 'http://localhost:8088'
username = 'ari-demo'
password = 'foobar'

client = ari.connect(url, username, password)

# Callback for StasisStart event
def on_start_cb(channel, event):
 
    c = channel.get('channel')
    print "%s has entered the application" % c.json.get('name')
    number = c.json.get('caller')['number']
    print "Number is %s" % number

    c.play(media='sound:your')
    c.play(media='sound:number')
    c.play(media='sound:is')
    c.play(media='digits:' + number)
    c.continueInDialplan()

# Callback for StasisEnd event
def on_end_cb(channel, event):
 
    print "%s has left the application" % channel.json.get('name')

client.on_channel_event('StasisStart', on_start_cb)
client.on_channel_event('StasisEnd', on_end_cb)

client.run(apps='ari-demo')
