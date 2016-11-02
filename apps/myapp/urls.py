from django.conf.urls import url
from django.views.generic import TemplateView

from apps.myapp import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='myapp/home.html')),
]
