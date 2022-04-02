from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader


def index(request):
    return render(request, 'index.html')

def lotto(request):
    import random
    
    pick = random.sample(range(1, 46), 6)
    #context ={
    #    'pick':pick
    #}


    return render(request, 'lotto.html', {'pick':pick})



    
