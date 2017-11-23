#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author：     wukai15937@gmail.com
Datetime：   2017/11/23 下午5:52
"""

from __future__ import unicode_literals, print_function, division, absolute_import

import os

if os.environ.get('DOCKER'):
    HOST = os.popen("/sbin/ip route|awk '/default/ { print $3 }'").read().strip('\n')
else:
    HOST = '127.0.0.1'

class mongo_conf(object):

    host = HOST
    port = 27017
    db = 'tc'

class redis_conf(object):

    host = HOST
    port = 23781

class ssdb_conf(object):

    host = HOST
    port = 22228
