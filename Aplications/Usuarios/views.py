from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
def register(request):
    
    if request.method == 'GET':
        try:
         print('No es por aca')
         
        except SyntaxError as e:
            print(e)
        
    else:
        print('Es por aca')
        

def prueba(request):
    
    return render(request,'hola.html')