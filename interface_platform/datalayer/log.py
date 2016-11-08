# -*- coding:utf-8 -*-
import os
import logging.config
from django.conf import settings


# 该函数实现的功能：传递一个要记录日志的文件名作为参数，默认是settings.py里的LOGGING中filename
def set_log_filename(file_name):
    # before use settings ,must set DJANGO_SETTINGS_MODULE
    os.environ['DJANGO_SETTINGS_MODULE'] = 'interface_platform.settings'
    logging_dic = settings.LOGGING
    logging_dic['handlers']['default']['filename'] = os.path.join(settings.LOG_ROOT, file_name)
    logging.config.dictConfig(logging_dic)
