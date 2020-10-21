""" Views for the layout application """

from django.http import request
from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .models import ZipUtilities
import django
import os


def home(request):
    """ Default view for the root """
    djangoversion = django.get_version()
    return render(request, 'layout/home.html', {'djangoversion': djangoversion})


def profile(request, path=None):
    # return render(request, "user/profile.html")
    if not path:
        path = "Release_Data/%s/" % request.user
    path_list = os.listdir(path)
    dirs = [x + '/' for x in path_list if os.path.isdir(path + x)]
    files = [x for x in path_list if os.path.isfile(path + x)]
    context = {"dirs": dirs, "files": files, "path": path}
    # print(path_list)
    # print(context)
    return render(request, "user/profile.html", context)


def check(request):
    """用于检测登录用户权限，并进行内容分发"""
    # return render(request, "user/profile.html")
    if str(request.user) == request.path.split(os.sep)[2]:
        # from pprint import pprint
        # pprint(request.__dict__)
        # [django三种文件下载方式 - W-D - 博客园](https://www.cnblogs.com/wdliu/p/8723981.html)
        path = request.path[1:]
        if os.path.isfile(path):
            file = open(path, 'rb')
            response = FileResponse(file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="%s"' % (
                os.path.basename(request.path))
            return response
        else:
            return profile(request, path)
    else:
        return HttpResponse("当前账户无权限访问")


def zipfile_down(request, path=None):
    if not path:
        path = "Release_Data/%s/" % request.user
    file_objs = os.listdir(path)
    utilities = ZipUtilities()
    for filename in file_objs:
        tmp_dl_path = os.path.join(path, filename)
        utilities.toZip(tmp_dl_path, filename)
    # utilities.close()
    response = StreamingHttpResponse(
        utilities.zip_file, content_type='application/zip')
    response['Content-Disposition'] = 'attachment;filename="%s.zip"' % request.user
    return response


# ------ [基于django的简单ftp实现_conquerwave的专栏-CSDN博客](https://blog.csdn.net/conquerwave/article/details/77775191)
class PathItem:
    name = ""
    parent = ""
    url = ""

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.url = "folder/" + os.path.join(parent, name)


class FileItem:
    name = ""
    parent = ""
    url = ""
    canRead = False

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.url = "file/" + os.path.join(parent, name)


def index(request):
    current = 'folder'
    context_dic = {}
    context_dic['current'] = current
    ps = os.listdir(current)
    path = []
    file = []
    for n in ps:
        v = os.path.join(current, n)
        if os.path.isdir(v):
            p = PathItem(n, current)
            path.append(p)
        else:
            f = FileItem(n, current)
            file.append(f)

    context_dic['path'] = path
    context_dic['file'] = file
    return render(request, 'index.html', context_dic)


def show_folder(request, url):
    current = url
    context_dic = {}
    context_dic['current'] = current
    ps = os.listdir(current)
    path = []
    file = []
    for n in ps:
        v = os.path.join(current, n)
        if os.path.isdir(v):
            p = PathItem(n, current)
            path.append(p)
        else:
            f = FileItem(n, current)
            file.append(f)

    #context_dic['parent'] = os.path.pardir(url)
    context_dic['path'] = path
    context_dic['file'] = file
    return render(request, 'index.html', context_dic)
