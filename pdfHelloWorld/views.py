from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.http import HttpResponse
from matplotlib import pylab
from pylab import *
from PIL import Image

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

def index(request):
    print("here we cal request")
    my_dictionary = {'insert_name' : "I am from view.py"}
    if(request.GET.get('mybtn')):
        #mypythoncode.mypythonfunction( int(request.GET.get('mytextbox')) )
        print("here called from my button")
    return render(request, 'pdfHelloWorld/index.html', context=my_dictionary)
def request_page(request):
    print("here we capture new request")
    if(request.GET.get('mybtn')):
        return render(request,'pdfHelloWorld/index.html')
def logout(request):
    print("logout called")
    return render(request,'pdfHelloWorld/index.html')