from django.http import HttpResponse

def home_view(request,*args, **kwargs):
    return HttpResponse("<h1>Hello this is my final master degree presentation."
                        "<img src=\"https://upload.wikimedia.org/wikipedia/commons/c/c8/Log%C3%B3tipo_do_Politecnico_de_Setubal.png\" alt=\"IPS\" width=\"500\" height=\"600\"></h1>")