# I have created this site for learning
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("HELLO, Welcome")
    para={'name':'Manav','place':'Bengaluru'}
    return render(request ,'index.html',para)

def analyze(request):
    text=request.GET.get('text','default')
    remove=request.GET.get('remove','off')
    upper=request.GET.get('upper','off')
    space = request.GET.get('space', 'off')
    ccount = request.GET.get('Character count', 'off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    ana=""
    if remove=='on':
        ana = ""
        for char in text:
            if char not in punctuations:
                ana = ana + char
        param={'Purpose':'Remove','Analyzedtext': ana}
        text=ana

    if upper=="on":
        ana = ""
        for char in text:
            if char.lower:
                ana = ana + char.upper()
        param={'Purpose':'Upper case','Analyzedtext': ana}
        text=ana

    if space=="on":
        ana = ""
        for char in text:
            if not char==" ":
                ana = ana + char
        param={'Purpose':'Without space','Analyzedtext': ana}
        text=ana

    if remove!='on' and upper!='on' and space!='on':
        return HttpResponse("Choose one of the option")

    return render(request,'analyze.html',param)
