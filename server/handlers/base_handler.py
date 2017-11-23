#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author：     wukai15937@gmail.com
Datetime：   2017/11/23 下午1:24
"""

from __future__ import unicode_literals, print_function, division, absolute_import

from tornado.web import RequestHandler

class BaseHandler(RequestHandler):

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

    def initialize(self, action=None):
        self.action = action.__name__ if callable(action) else action
        super(BaseHandler, self).initialize()

    def prepare(self):
        super(BaseHandler, self).prepare()
        args = {k.lower(): v for k, v in self.request.headers.items()}
        args.update({k: v for k, v in self.request.arguments.items()})
        self._all_arguments = args

    def get(self, *args, **kwargs):
        return super(BaseHandler, self).get(*args, **kwargs) if not self.action \
            else getattr(self, self.action)(*args, **kwargs)

    def post(self, *args, **kwargs):
        return super(BaseHandler, self).post(*args, **kwargs) if not self.action \
            else getattr(self, self.action)(*args, **kwargs)

    def put(self, *args, **kwargs):
        return super(BaseHandler, self).put(*args, **kwargs) if not self.action \
            else getattr(self, self.action)(*args, **kwargs)

    def patch(self, *args, **kwargs):
        return super(BaseHandler, self).patch(*args, **kwargs) if not self.action \
            else getattr(self, self.action)(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return super(BaseHandler, self).delete(*args, **kwargs) if not self.action \
            else getattr(self, self.action)(*args, **kwargs)

    def options(self, *args, **kwargs):
        self.write_success()

    def write_success(self, data=None):
        self.write({'errcode': 0, 'errmsg': 'success', 'data': data})

    @property
    def current_user(self):
        return super(BaseHandler, self).current_user

    def get_current_user(self):
        current_user = None
        return current_user

    def get_all_arguments(self):
        return self._all_arguments

    def get_argument(self, name, default=None):
        return self._all_arguments.get(name, default)