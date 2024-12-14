from django.http import HttpResponse

def home_view(request,*args, **kwargs):
    return HttpResponse("<h1>Ola , Hoje dia 14 eu vou fazer deploy da minha aplicacao web</h1>")