from django.contrib import admin
from django.urls import path
from myapp.views import home_view  # Correct the path to match your app

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
]
