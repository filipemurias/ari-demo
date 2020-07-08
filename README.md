# About
This is a small demo in Python for [Asterisk REST interface (ARI)](https://wiki.asterisk.org/wiki/pages/viewpage.action?pageId=29395573).

Uses [Asterisk ARI Python library](https://github.com/asterisk/ari-py).

# Installation
* Install Python ARI library with `pip install ari`
* Clone code from git repository with `git clone https://github.com/filipemurias/ari-demo.git`
* Update your Asterisk details (URL, username and password) in deamon.py
* Run `python deamon.py`

# Asterisk configuration
## Enable HTTP server in http.conf
```
[general]
enabled = yes
bindaddr = 0.0.0.0
bindport = 8088
```
## Enable ARI and create an user in ari.conf
```
[general]
enabled = yes
pretty = yes
; Allow access from localhost only
allowed_origins = localhost:8088
 
[ari-demo]
type = user
read_only = no
password = foobar
```
## Update the dialplan in extensions.conf
```
[ARI demo]
; Dial any 6 digits number to execute the ARI application
exten => _XXXXXX,1,Answer
exten => _XXXXXX,n,Stasis(ari-demo)
exten => _XXXXXX,n,Hangup
```
