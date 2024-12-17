from django.http import HttpResponse

def home_view(request,*args, **kwargs):
    return HttpResponse("<h1>Hoje estou a apresentar a minha tese de mestrado. Guilherme 17/12/2024</h1>")