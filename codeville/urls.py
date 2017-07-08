from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.create_user, name='create_user'),
    url(r'^contributors$', views.contributors, name='contributors'),
    url(r'add', views.add, name="add"),
]
