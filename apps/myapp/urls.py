from django.conf.urls import url
from apps.myapp import views

urlpatterns = [
    url(r'', views.index, name='index')
]
