from django.shortcuts import render

def home(request):
     
    x = 'Olá mundo!'
    return render(request, 'index.html',)

