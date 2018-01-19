from django.conf.urls import url, include

from . import views


urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^product/(?P<name>[0-9A-Za-z\-]+)/$', views.product_details, name='product_details'),
    url(r'^buyer/(?P<owner>[0-9A-Za-z]+)/$', views.buyer_details, name='buyer_details'),
    #url(r'^buyer\/(?P<owner>[a-zA-Z0-9]+)/$', views.buyer_details, name='buyer_details'),
]
