#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author：     wukai15937@gmail.com
Datetime：   2017/11/23 下午1:24
"""

from __future__ import unicode_literals, print_function, division, absolute_import

from .rest_handler import RestHandler

class IndexHandler(RestHandler):

    def index1(self):
        print(self.current_user, self._all_arguments)
        self.write_success()

    def index(self, *args, **kwargs):
        print('get')

