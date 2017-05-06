from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from crowd import views

urlpatterns = [
    url(r'^$', views.HelloView.as_view(), name="hw"),
    url(r'^test/$', views.TestView.as_view(), name="hw2"),

    url(r'^products/$', views.ProductListView.as_view(), name='product-list'),


]
