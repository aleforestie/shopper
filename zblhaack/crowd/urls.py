from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from crowd import views

urlpatterns = [
    url(r'^$', views.HelloView.as_view(), name="hw"),
    url(r'^test/$', views.TestView.as_view(), name="hw2"),

    url(r'^products/$', views.ProductListView.as_view(), name='product-list'),
    url(r'^products/ask/$', views.ProductAskView.as_view(), name='product-ask'),
    url(r'^products/choose/$', views.ChooseView.as_view(), name='product-choose'),
    url(r'^products/display/$', views.DisplayView.as_view(), name='product-display'),

    url(r'^products/ask/ajaxYes/(?P<pk>[0-9]+)/$',
        views.AjaxYes.as_view(),
        name='ajax-yes'),


]
