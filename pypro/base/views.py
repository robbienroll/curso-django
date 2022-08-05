# from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'base/home.html')
    # return HttpResponse('<html><body>Hello Mr Django</body></html>', content_type='text/html')
