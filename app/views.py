from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':1909,'b':2009,'c':2050}
    return render(request,'conditions.html',context=d)


def loops(request):
    d={'name':'Renu'}
    return render(request,'loops.html',d)
