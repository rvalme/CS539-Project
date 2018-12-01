from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import ZipStarbuck
# Create your views here.

def index(request):
    zip_list = ZipStarbuck.objects.order_by('zipcode')
    zip_dict = {'zip_starbucks':zip_list}
    my_dict = {'insert_me':"Now I am coming from first_app/index.html"}
    return render(request, 'first_app/index.html', context=zip_dict)
