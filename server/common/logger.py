#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author：     wukai15937@gmail.com
datetime：   2017/10/15 下午11:30
"""

from __future__ import absolute_import, division, print_function, \
    unicode_literals


import os
import logging
import colorlog

def init_logger():
    formatter = colorlog.ColoredFormatter(
        '%(log_color)s%(asctime)s.%(msecs)04d %(levelname)-10s %(name)-20s %(message)s',
        datefmt='%Y-%m-%dT%H:%M:%S',
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    )

    file_formatter = logging.Formatter(
        fmt='%(asctime)s.%(msecs)04d %(levelname)-10s %(name)-20s %(message)s',
        datefmt='%Y-%m-%dT%H:%M:%S'
    )

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.handlers[0].setFormatter(formatter)

    file_handler = logging.handlers.TimedRotatingFileHandler(
        filename=os.path.join(os.path.dirname(__file__), '../../logs/log.txt')
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    logger.info('initialized Logger success.')
