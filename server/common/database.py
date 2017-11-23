#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author：     wukai15937@gmail.com
Datetime：   2017/11/23 下午5:50
"""

from __future__ import unicode_literals, print_function, division, absolute_import

from pymongo import MongoClient
from redis import Redis
from pyssdb import Client as SSDBClient

from server.config.conf import mongo_conf, ssdb_conf, redis_conf

class MongoConn(object):
    @classmethod
    def instance(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        assert not hasattr(self.__class__, '_instance'), 'Do not instantiate directly!'
        host = mongo_conf.host
        port = mongo_conf.port
        db = mongo_conf.db
        self.client = MongoClient(host=host, port=port)
        self.db = self.client[db]
        self.test_coll = self.db['test']

class SSDBConn(object):
    @classmethod
    def instance(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        assert not hasattr(self.__class__, '_instance'), 'Do not instantiate directly!'
        host = ssdb_conf.host
        port = ssdb_conf.port
        self.conn = SSDBClient(host=host, port=port)

class RedisConn(object):
    @classmethod
    def instance(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        assert not hasattr(self.__class__, '_instance'), 'Do not instantiate directly!'
        host = redis_conf.host
        port = redis_conf.port
        self.conn = Redis(host=host, port=port)

if __name__ == '__main__':
    mongo = MongoConn.instance()
    mongo.test_coll.insert({'hello': 'world'})
    h = mongo.test_coll.find_one()
    print(h)

    ssdb = SSDBConn.instance().conn
    ssdb.set('h', 'hello, world')
    print(ssdb.get('h'))

    redis = RedisConn.instance().conn
    redis.set('h', 'hello, world')
    print(redis.get('h'))
