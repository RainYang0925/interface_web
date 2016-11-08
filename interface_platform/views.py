# -*- coding: UTF-8 -*-

from models import *
from account.models import Account
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
# from django.contrib.sessions import
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView

meta = {'code': 0, 'message': ''}
data = {}
ret = {'meta': meta, 'data': data}


def test(request):
    text = """<h1>welcome to my app!</h1>"""
    return HttpResponse(text)


# 建议因为是重定向，暂采取重新登录处理该情况
# 结果是因为自己少传了一个request变量导致的
def get_projects(request, project_id):
    if request.user.is_authenticated():
        user = request.user
        print user.id
        # print request.session
        d = {'key': user.id, 'param': project_id}
        return render(request, 'test.html', d)


# 返回所有项目名称
class ProjectsView(TemplateView):
    template_name = "test.html"

    # def get(self, request, *args, **kwargs):
    #     ctx = self.get_context_data()
    #     return self.render_to_response(ctx)

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated():
            user = self.request.user
            # print kwargs
            print user.id
            context = super(ProjectsView, self).get_context_data(**kwargs)
            context['d'] = {'key': user.id}
            print context['project_id']
            return context

# def project_interfaces_header(request, project_id, it_id):
#     if request.method == 'POST':
#         name = request.POST['name']
#         value = request.POST['value']
#         desc = request.POST['desc']
#         header_type = int(request.POST['header_type'])
#
#     header = ItHeader(name=name, value=value, desc=desc, it_id=it_id, header_type=header_type)
#     header.save()
#     h = ItHeader.objects.get(it_id=it_id)
#
#     if h.name == name and h.value == value and h.desc == desc and header_type == header_type:
#         data['name'] = h.name
#         data['value'] = h.value
#         data['desc'] = h.desc
#         data['header_type'] = h.header_type
#         meta['code'] = 201
#         meta['message'] = "创建成功"
#
#     return render_to_response('test.html', {'result': ret})
