from django.http import HttpResponse

def home_view(request,*args, **kwargs):
    return HttpResponse("<h1>Guilherme Malhado: Hello this is my presentation.</h1>")