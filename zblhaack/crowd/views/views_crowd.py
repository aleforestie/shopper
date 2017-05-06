from django.shortcuts import render, get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import TemplateView, DeleteView, View
from django.contrib.messages.views import SuccessMessageMixin

from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy

class HelloView(TemplateView):
    template_name = "crowd/hello.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
