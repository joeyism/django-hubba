from django.conf.urls import url, include

from . import views


urlpatterns = [
    url('', views.index, name='index'),
    url(r'^(?P<name>[0-9A-Za-z\-]+)/$', views.product_details, name='product_details'),
]
