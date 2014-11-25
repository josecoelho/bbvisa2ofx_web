BBVisa2OFX Web
==============

[![Build Status](https://travis-ci.org/josecoelho/bbvisa2ofx_web.svg?branch=master)](https://travis-ci.org/josecoelho/bbvisa2ofx_web)

This project is a web interface of
https://github.com/josecoelho/bbvisa2ofx

Running on: http://bbvisa2ofx.josecoelho.com


Dependencies
------------

* web.py -> http://webpy.org/
* bbvisa2ofx -> https://github.com/josecoelho/bbvisa2ofx


Run local
------------

$ python service.py

How to contribute
------------------
- Clone this project
- Create a branch for the fix or feature
- Commit your changes
- Send a pull request of your branch

Thanks!

Development
-------------

### Upgrading...

Change versions of dependencies on requirements.txt

Activate virtualenv:
```
  $ source ./venv/bin/activate
```

Upgrade dependencies
```
  pip install -r requirements.txt --upgrade
```

Commit your changes and publish to heroku
```
  git push heroku master
```
