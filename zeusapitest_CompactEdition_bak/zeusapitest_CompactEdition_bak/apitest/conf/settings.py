#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
__author__ = 'zhangbiao'
__date__ = '2014-02-28'


config_dict_template = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s--%(levelname)s--%(filename)s-[line:%(lineno)para_dict]-%(module)s.%(name)s ---- %(message)s',
            'datefmt': '%Y-%m-%para_dict %H:%M:%S'
        },
        'simple': {
            'format': '%(asctime)s - %(levelname)s - %(message)s'
        },
        'mail': {
            'format': '%(asctime)s : %(message)s',
            'datefmt': '%Y-%m-%para_dict %H:%M:%S'
        },
    },
    'handlers': {
        'default': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': '',
            'maxBytes': 50 * 1024 * 1024,
            'backupCount': 10
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout',
            'level': 'ERROR',
        },
        'mail': {
            'class': 'logging.handlers.SMTPHandler',
            'level': 'CRITICAL',
            'formatter': 'mail',
            'mailhost': 'smtp.exmail.qq.com',
            'fromaddr': 'test_env@lightinthebox.com',
            'toaddrs': ['zhangbiao@lightinthebox.com'],
            'subject': '[mail] Error encountered.',
            'credentials': ('test_env@lightinthebox.com', 'auto@litb!2013')
        },
    },
    'loggers': {
        'mail': {
            'handlers': ['mail'],
            'level': 'CRITICAL',
            'propagate': False
        },
    },
    'root': {
        'handlers': ['default'],
        'level': 'DEBUG'
    },
}
