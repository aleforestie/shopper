from django.shortcuts import render, get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import TemplateView, DeleteView, View
from django.contrib.messages.views import SuccessMessageMixin

from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy

from crowd.models import Product

class HelloView(TemplateView):
    template_name = "crowd/hello.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})



class TestView(TemplateView):
    template_name = "crowd/test.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

class ProductListView(ListView):
    model = Product
    template_name = 'crowd/productList.html'

    """def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]""" #Pour filtrer la liste
