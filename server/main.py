#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author：     wukai15937@gmail.com
datetime：   2017/10/13 下午4:34
"""

from __future__ import absolute_import, division, print_function, \
    unicode_literals

import os
import site
import logging
import multiprocessing

site.addsitedir(os.path.abspath(os.path.dirname('../')))

import tornado
from tornado import web
from tornado.options import options, define
from tornado import log as t_log


def gen_handlers():
    '''
    :return: route table
    '''
    return [

    ]

class ServerApp(web.Application):
    '''A collection of request handlers that make up a web application.
    '''

    def __init__(self):
        super(ServerApp, self).__init__(
            handlers=gen_handlers(),
            **dict()
        )

def run(port):
    app = ServerApp()
    app.listen(port)
    logging.info('server run at port: {}'.format(port))
    tornado.ioloop.IOLoop.instance().start()

def main():
    define('port', default='8888', type='str', metavar='PORT', help='server port')

    logging.getLogger().setLevel(logging.DEBUG)
    t_log.app_log.setLevel(logging.DEBUG)
    t_log.gen_log.setLevel(logging.DEBUG)
    t_log.access_log.setLevel(logging.DEBUG)

    port = options.port
    if str(port).isdigit():
        run(int(port))
    else:
        port_list = list(map(int, port.split(',')))

        for p in port_list:
            multiprocessing.Process(target=run, args=(p,)).start()



if __name__ == '__main__':
    main()
