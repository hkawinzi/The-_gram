from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from .forms import LoginForms
 
def get-name(request):
    #post request that processes the data from the form
    if request.method == 'POST':
        form = LoginForms(request.POST)