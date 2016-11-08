# -*- coding: UTF-8 -*-

# 接口body部分
class Body(object):
    def __init__(self, body_id, name, value_type, value, it_id, body_type, desc=None):
        self.id = body_id
        self.name = name
        self.type = value_type
        self.desc = desc
        self.value = value
        self.it_id = it_id
        self.body_type = body_type
