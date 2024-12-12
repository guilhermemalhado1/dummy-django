from django.http import HttpResponse

def home_view(request,*args, **kwargs):
    return HttpResponse("<h1>Hello World from Tese Mestrado</h1>")