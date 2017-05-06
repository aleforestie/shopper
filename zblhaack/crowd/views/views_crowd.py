from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import TemplateView, DeleteView, View
from django.contrib.messages.views import SuccessMessageMixin

from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy

from django.db.models import F
from crowd.models import Product, FavoriteColor, FavoriteBrand, FavoriteFamily

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

    def get_queryset(self):
        return Product.objects.order_by('popularity').reverse()[:10]

class ProductAskView(TemplateView):
    template_name = 'crowd/productAskList.html'

    def get(self, request, *args, **kwargs):
        #changer le filter
        products = Product.objects.filter()
        pks = []
        for i in products:
            pks.append(i.pk)
        return render(request, self.template_name, {'products':products, 'pks':pks,})

    def post(self, request, *args, **kwargs):
        products = Product.objects.filter()
        color = request.POST.get('color', '')
        brand = request.POST.get('brand', '')
        family = request.POST.get('family', '')
        if color:
            products = products.filter(main_color=color)
            lol = FavoriteColor.objects.get(pk=1)
            if color == 'red':
                lol.red = F('red') + 1
            if color == 'blue':
                lol.blue = F('blue') + 1
            if color == 'black':
                lol.black = F('black') + 1
            if color == 'white':
                lol.white = F('white') + 1
            lol.save()
        if brand:
            products = products.filter(brand=brand)
            lol = FavoriteBrand.objects.get(pk=1)
            if brand == 'hype brand':
                lol.hype_brand = F('hype_brand') + 1
            if brand == 'alf brand':
                lol.alf_brand = F('alf_brand') + 1
            if brand == 'annick brand':
                lol.annick_brand = F('annick_brand') + 1
            lol.save()
        if family:
            products = products.filter(family=family)
            lol = FavoriteFamily.objects.get(pk=1)
            if family == 't-shirt':
                print(lol.t_shirt)
                lol.t_shirt = F('t_shirt') + 1
                print(lol.t_shirt)
            if brand == 'jacket':
                lol.jacket = F('jacket') + 1
            if brand == 'sport shoe':
                lol.sport_shoe = F('sport_shoe') + 1
            if brand == 'pants':
                lol.pants = F('pants') + 1
            lol.save()

        pks = []
        for i in products:
            pks.append(i.pk)
        return render(request, self.template_name, {'products':products, 'pks':pks,})

class AjaxYes(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk', '-1')
        pr = get_object_or_404(Product, pk=pk)
        pr.popularity = F('popularity') + 1
        pr.save()
        data = {
            'ok':True,
        }
        return JsonResponse(data)

    #Ameliorer avec un vrai inaccessible si get
    def get(self, request, *args, **kwargs):
        get_object_or_404(Favorite, pk=-1)

class ChooseView(TemplateView):
    template_name = 'crowd/choose.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

class DisplayView(TemplateView):
    template_name = 'crowd/display.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
