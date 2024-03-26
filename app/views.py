from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView

from app.models import Sinf, Kunlar, Fan, Sinfnom
from .models import Sinf


class Malumot(TemplateView):
    template_name = "index.html"


class Base(ListView):
    model = Sinf
    template_name = 'homepage.html'


# Create your views here.
def members(request):
    mymembers = Sinf.objects.all().values()
    kun = Kunlar.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'mymembers': mymembers,
        'kun': kun
    }
    return HttpResponse(template.render(context, request))


class CategoryView(View):
    def get(self, request, sinf):
        sinf = get_object_or_404(Sinf, title=sinf)
        return render(request, "home.html", {"sinf": sinf})


class SinfView(View):
    def get(self, request, sinf, sinfnom):
        sinf = get_object_or_404(Sinf, title=sinf)
        sinfnom = get_object_or_404(Sinfnom, nomi=sinfnom)
        return render(request, 'index.html', {'sinf': sinf, 'sinfnom': sinfnom})


class ProView(View):
    def get(self, request, sinfi, sinfnom, kun):
        kun = get_object_or_404(Kunlar, nom=kun)
        sinflar = get_object_or_404(Sinf, title=sinfi)
        sinfnom = get_object_or_404(Sinfnom, nomi=sinfnom)
        fanlar = Fan.objects.filter(sinf=sinflar, kun=kun)
        return render(request, "index.html", {'sinf': sinflar, 'sinfnom': sinfnom, 'kun': kun, "fanlar": fanlar})
