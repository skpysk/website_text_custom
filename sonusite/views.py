
from django.http import HttpResponse # fix error str objecrt has not get wala
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('re','off') # yeh checkbox ke leyai hai # secound argument adjust 
    caps=request.POST.get('cap','off')
    rem=request.POST.get('rem','off')
    space=request.POST.get('space','off')
    count=request.POST.get('count','off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyzwd.html', params)
    if(caps == "on") :
        analy = ""
        for i in djtext:
            analy = analy + i.upper()
            params = {'purpose': 'campitalied', 'analyzed_text': analy}
            djtext = analy
        #return render(request, 'analyzwd.html', params)
    if(rem == "on") :
        analy = ""
        for i in djtext:
            if i !="\n" and i != "\r":
             analy = analy + i
            params = {'purpose': 'remobed liner', 'analyzed_text': analy}
            djtext = analy
        #return render(request, 'analyzwd.html', params)
    if(space == "on") :
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        #return render(request, 'analyzwd.html', params)
    if(count == "on") :
        x = [djtext.split(" ")]
        for i in x :

            params = {'purpose': 'total characters found', 'analyzed_text':len(i)}
        #return render(request, 'analyzwd.html', params)
    
    return render(request, 'analyzwd.html', params)