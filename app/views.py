from django.shortcuts import render
import json
from django.http import HttpResponse


def index(request):
    """
    index
    """

    context = {'title': 'タイトルです',
               }

    return render(request, 'app/index.html', context)


def index2(request):
    """
    index2
    """

    context = {'title': 'タイトルです',
               }

    return render(request, 'app/index2.html', context)


def index3(request):
    """
    index3
    """

    context = {'title': 'タイトルです',
               }

    return render(request, 'app/index3.html', context)


def api_01(request):
    """
    getでkeywordを受け取り、jsonを返すAPI
    """

    dctData = {}

    # keywordがgetで与えられたとき(辞書のkeyが存在したら)
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        dctData['原型'] = keyword
        dctData['丁寧語'] = keyword+'でございます'
        dctData['疑問'] = keyword+'?'
    else:
        dctData['データ'] = 'なし'

    return HttpResponse(
        json.dumps(dctData, ensure_ascii=False),
        content_type='application/json; charset=utf-8',
    )
