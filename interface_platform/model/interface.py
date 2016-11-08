# -*- coding: UTF-8 -*-

from header import Header
from body import Body


# 接口类主体
class Interface(object):
    def __init__(self, it_id, name, protocol_type, request_type, path, project_id, author, host_id, status,
                 responsible, desc=None):
        self.id = it_id
        self.name = name
        self.protocol_type = protocol_type
        self.request_type = request_type
        self.path = path
        self.desc = desc
        self.project_id = project_id
        self.author = author
        self.host_id = host_id
        self.status = status
        self.responsible = responsible

    # headers和bodys都用list存储
    @property
    def headers(self):
        return self.headers

    @headers.setter
    def headers(self, header_id, name, value, it_id, header_type, desc=None):
        header = Header(header_id, name, value, it_id, header_type, desc)
        self.headers.append(header)

    @property
    def bodys(self):
        return self.bodys

    @bodys.setter
    def bodys(self, body_id, name, value_type, value, it_id, body_type, desc=None):
        body = Body(body_id, name, value_type, value, it_id, body_type, desc)
        self.bodys.append(body)
