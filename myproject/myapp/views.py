from django.http import HttpResponse

def home_view(request,*args, **kwargs):
    return HttpResponse("<h1>Hello World From Tese Mestrado 2024 GM</h1>")