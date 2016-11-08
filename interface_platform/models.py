# -*- coding: utf-8 -*-
from django.db import models
# from django.contrib.auth.models import settings.AUTH_USER_MODEL
from account.conf import settings
from account.models import Account

REQUEST_TYPE_CHOICES = {
    ('POST', 'POST'),
    ('GET', 'GET'),
    ('PUT', 'PUT'),
    ('DELETE', 'DELETE'),
    ('PATCH', 'PATCH'),
    ('HEAD', 'HEAD'),
    ('OPTIONS', 'OPTIONS'),
    ('TRACE', 'TRACE')
}

PROTOCOL_TYPE_CHOICES = {
    ('HTTP', 'HTTP'),
    ('HTTPS', 'HTTPS')
}


# 项目表
class Project(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=254)
    user = models.ForeignKey(Account)  # 项目所属用户

    def __unicode__(self):
        return self.name


# 项目变量表
class Variable(models.Model):
    name = models.CharField(max_length=100)  # 项目的变量名
    desc = models.CharField(max_length=254)
    value = models.CharField(max_length=254)
    project = models.ForeignKey(Project)  # 外建项目Project，表示该变量所属于的项目
    type = models.IntegerField()

    def __unicode__(self):
        return self.name


# 接口详情表
class ITStatement(models.Model):
    name = models.CharField(max_length=100)  # 接口名称
    protocol_type = models.CharField(max_length=10, choices=PROTOCOL_TYPE_CHOICES)
    request_type = models.CharField(max_length=10, choices=REQUEST_TYPE_CHOICES)
    path = models.CharField(max_length=100)
    desc = models.CharField(max_length=254)
    project = models.ForeignKey(Project)  # 表示所属项目
    creator = models.ForeignKey(Account, related_name="creator")  # 创建者
    host = models.ForeignKey(Variable)  # HOST变量
    # host_id = models.IntegerField()  # HOST变量
    status = models.SmallIntegerField()  # 接口执行状态 0:执行失败  1:执行成功  2:未执行
    responsible = models.ForeignKey(Account, related_name="responsible")  # 负责人
    timestamp = models.DateTimeField('最后修改时间', auto_now=True)  # 最后一次修改的时间

    def __unicode__(self):
        return self.name


# 接口body表，即请求或响应体，用body_type区分
class ITBody(models.Model):
    name = models.CharField(max_length=100)  # 参数名
    type = models.IntegerField()  # 参数类型
    desc = models.CharField(max_length=254)
    value = models.CharField(max_length=254)
    it = models.ForeignKey(ITStatement)
    # 外建接口ItStatement，表示该body所属于的接口
    body_type = models.SmallIntegerField()  # 1:请求体  2:响应体

    def __unicode__(self):
        return self.name


# 接口头表，即请求或响应头，用header_type区分
class ITHeader(models.Model):
    name = models.CharField(max_length=100)  # 参数名
    value = models.CharField(max_length=254)
    desc = models.CharField(max_length=254)
    it = models.ForeignKey(ITStatement)
    header_type = models.IntegerField()

    def __unicode__(self):
        return self.name


# 接口日志表
class ITLog(models.Model):
    it = models.OneToOneField(ITStatement)  # 外建接口ITStatement，表示该日志所属于的接口
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)
    log_path = models.CharField(max_length=254)

    def __unicode__(self):
        return self.name


# 目录树表，表示项目与测试用例的关系
class DirectoryTree(models.Model):
    parent = models.IntegerField()
    name = models.CharField(max_length=254)
    key = models.CharField(max_length=100)
    # key 表示 节点经过其父节点的id键值，一直迭代到根节点（不包括该节点的），用来记录从根节点到该节点的路径
    level = models.IntegerField()
    project = models.ForeignKey(Project)
    # 目录项属于哪一个项目，关联Project表的主键

    def __unicode__(self):
        return self.name


# 测试用例表
class TestCase(models.Model):
    name = models.CharField(max_length=254)
    belong = models.ForeignKey(DirectoryTree)
    # 测试用例属于哪个目录项，关联DirectoryTree表的主键
    status = models.SmallIntegerField()  # 接口执行状态 0:执行失败  1:执行成功  2:未执行
    author = models.ForeignKey(Account)  # 作者
    responsible = models.IntegerField()  # 负责人
    timestamp = models.DateTimeField('最后一次修改时间', auto_now=True)  # 最后一次修改的时间
    tags = models.CharField(max_length=254)  # 标签

    def __unicode__(self):
        return self.name


# 测试用例里的接口执行顺序流，即接口集组成一个test case
class TestCaseStep(models.Model):
    tc = models.ForeignKey(TestCase)  # 外建关联TestCase，表示该项属于哪个test case
    it = models.ForeignKey(ITStatement)  # 外键关联ITStatement，表示该项是哪个接口
    index = models.IntegerField()  # 记录接口执行的步骤
    name = models.CharField(max_length=100)  # 可对接口集重命名

    def __unicode__(self):
        return self.name


# 测试用例日志表
class TestCaseLog(models.Model):
    tc = models.OneToOneField(TestCase)  # 外键关联TestCase，表明是哪个test case 的日志
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)
    log_path = models.CharField(max_length=254)

    def __unicode__(self):
        return self.name


# 标签表
class Tag(models.Model):
    name = models.CharField(max_length=254)
    num = models.IntegerField()  # 标签被引用的次数

    def __unicode__(self):
        return self.name


# 标签与test case 映射表
class TagMap(models.Model):
    tag = models.ForeignKey(Tag)  # 外键关联Tag，表明是哪个tag
    tc = models.ForeignKey(TestCase)  # 外键关联TestCase，表明是哪个test case

    def __unicode__(self):
        return self.tc.name
