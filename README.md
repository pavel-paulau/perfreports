perfreports
===========

[![Build Status](https://travis-ci.org/pavel-paulau/perfreports.svg?branch=master)](https://travis-ci.org/pavel-paulau/perfreports)

**perfreports** is the simplest way to generate HTML reports based on [perfkeeper](https://github.com/pavel-paulau/perfkeeper) data.


Requirements
------------

* Python 3.4 (e.g., python3-dev package for modern Ubuntu or [this](https://www.digitalocean.com/community/tutorials/how-to-set-up-python-2-7-6-and-3-3-3-on-centos-6-4) for CentOS 6.x)
* virtualenv

Running webapp
--------------

Assuming that perfkeeper database (MongoDB or TokuMX) is running on the same machine:

    $ make
    $ make run

The command above will start HTTP listener on port 5000.
