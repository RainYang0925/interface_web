# -*- coding: UTF-8 -*-

# 接口header部分
class Header(object):
    def __init__(self, header_id, name, value, it_id, header_type, desc=None):
        self.id = header_id
        self.name = name
        self.value = value
        self.desc = desc
        self.it_id = it_id
        self.header_type = header_type

