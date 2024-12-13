from django.http import HttpResponse

def home_view(request,*args, **kwargs):
    return HttpResponse("<h1>Welcome to my presentation</h1>")