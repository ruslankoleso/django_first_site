
from django.contrib import admin
from django.urls import path, include
from myapp.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dekatlon/',include('myapp.urls', namespace='myapp'))
]
