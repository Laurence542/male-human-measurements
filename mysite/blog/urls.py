from django.conf.urls.static import static
from . import views
from django.urls import path 


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('index', views.index, name='index'),
    path('register/',views.register, name = "register"),
    
]