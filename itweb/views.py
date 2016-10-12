# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import IT, NewIT
from forms import ITForm




def home(request):
    return render(request, 'base.html', get_its())


# 处理添加接口信息操作
def add_it(request):
    if request.POST:
        it_name = request.POST['itName']
        host = request.POST['host']
        request_type = request.POST['requestType']
        url = request.POST['url']
        args = request.POST['args']

        new_it = IT.objects.create(it_name=it_name, host=host, request_type=request_type, url=url, args=args)
        new_it.save()

    return render(request, 'base.html', get_its())


def create_it(request):
    return render(request, 'create_it.html')


def it_details(request):
    dict_it = {}
    if request.POST:
        it_name = request.POST['it-name']
        protocol_type = request.POST['protocol-type']
        request_type = request.POST['request-type']
        url = request.POST['url']
        desc = request.POST['desc']
        team = request.POST['team']
        person = request.POST['person']
        it = NewIT.objects.filter(it_name=it_name)
        if it is None:
            new_it = NewIT.objects.create(it_name=it_name, protocol_type=protocol_type, request_type=request_type,
                                          url=url, desc=desc, team=team, author=person)
            new_it.save()
            dict_it = {'new_it': new_it}
        else:
            dict_it = {'new_it': it}
    # if request.POST:
    #     it_form = ITForm(request.POST)
    #     print it_form.is_valid()
    #     new_it = it_form.save()
    #     print new_it
    print dict_it
    return render(request, 'it_details.html', dict_it)


def manage_it(request):
    return render(request, 'manage_it.html', get_its())


# 从数据库更新已有接口集
def get_its():
    table_data = {'it_table': IT.objects.all()}
    return table_data
