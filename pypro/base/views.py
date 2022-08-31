from django.shortcuts import render


def home(request):
    # return render(request, 'base/home.html', {'MODULOS':['test1','test2',]})
    return render(request, 'base/home.html', {})
