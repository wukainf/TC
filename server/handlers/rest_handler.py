#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author：     wukai15937@gmail.com
Datetime：   2017/11/23 下午3:21
"""

from __future__ import unicode_literals, print_function, division, absolute_import

import abc

from .base_handler import BaseHandler

class RestHandler(BaseHandler):
    '''防止不想要的http方法重写覆盖了action执行'''

    def get(self, *args, **kwargs):
        if self.action:
            return super(RestHandler, self).get(*args, **kwargs)
        else:
            return self.index()

    def post(self, *args, **kwargs):
        if self.action:
            return super(RestHandler, self).post(*args, **kwargs)
        else:
            return self.create()

    def patch(self, *args, **kwargs):
        if self.action:
            return super(RestHandler, self).patch(*args, **kwargs)
        else:
            return self.update()

    def put(self, *args, **kwargs):
        if self.action:
            return super(RestHandler, self).put(*args, **kwargs)
        else:
            return self.update()

    def delete(self, *args, **kwargs):
        if self.action:
            return super(RestHandler, self).delete(*args, **kwargs)
        else:
            return self.drop()

    @abc.abstractclassmethod
    def index(self):
        pass

    @abc.abstractclassmethod
    def create(self):
        pass

    @abc.abstractclassmethod
    def update(self):
        pass

    @abc.abstractclassmethod
    def drop(self):
        pass
