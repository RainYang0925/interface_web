# -*- coding: UTF-8 -*-

# 接口测试用例类
class TestCase(object):
    def __init__(self, testcase_id, name, status, responsible, tags=None):
        self.id = testcase_id
        self.name = name
        self.status = status
        self.responsible = responsible
        self.tags = tags

    # 根据testcase_id查testcase_step表获取所有执行步骤（接口）
    # 查到所有步骤，按照it_index递增顺序取出
    def get_steps(self):
        pass

    # 运行用例，记录测试日志
    def run(self):
        pass
