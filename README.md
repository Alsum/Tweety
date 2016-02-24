# Tweety

Django App Get the latest tweets for any screen name
using latest twitter REST APi 1.1

### Version
1.0

### Demo

* First you need to create twitter application
https://apps.twitter.com/app/new

* Then fill the following in settings.py file
```sh
TWITTER_CONSUMER_KEY = ""
TWITTER_CONSUMER_SECRET = ""
TWITTER_OAUTH_TOKEN = ""
TWITTER_OAUTH_TOKEN_SECRET = ""
```
* After download files

* Enter this Directory
```sh
$ cd src/
```
```sh
db.sqlite3  manage.py  requirments.txt  static_in_pro  templates  tweetsapp  tweety
```
* install requirments.txt
```sh
$ pip install -r requirments.txt
```
* migrate data base
```sh
$ python manage.py migrate
```
* Now you are ready to run this application

```sh
$ python manage.py runserver
```

```sh
System check identified no issues (0 silenced).
February 10, 2016 - 14:38:56
Django version 1.8, using settings 'tweety.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

![Alt text](src/sh.png?raw=true "Screenshot img")
