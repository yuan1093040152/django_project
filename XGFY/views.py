from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    info = models.XGFY_SQL.objects.all()
    return render(request,'XGFY/index.html',{'haha':info})

def DjangTest(request):
    #判断是否为空和是否为数字
    if request.method=='GET':
        gb = request.GET.get('modules1')
        if gb is  None:
            gb1 = '1,2'
        elif str.isdigit(gb)==True:
            gb1 = gb
        else:
            gb1 = '1,2'

        print('gb1=',gb1)

        gj = request.GET.get('username')
        #判断是否为空字符串和是否为空
        if gj is None:
        # if len(gj)==0:

        # if gj=='' and gj is None:
            info = models.XGFY_SQL.objects.raw('SELECT * FROM xgfy_xgfy_sql WHERE nationality IN (%s)'%gb1)

        elif len(gj)==0:
            info = models.XGFY_SQL.objects.raw('SELECT * FROM xgfy_xgfy_sql WHERE nationality IN (%s)' % gb1)
        else:

            info = models.XGFY_SQL.objects.raw('SELECT * FROM xgfy_xgfy_sql WHERE nationality IN (%s) AND country IN ("%s")'%(gb1,gj))

        print('gj=',gj)

        # info = models.XGFY_SQL.objects.filter(nationality=gb,country=gj)
        print(info)
        return render(request,'XGFY/DjangoTest01.html',{'haha':info})
