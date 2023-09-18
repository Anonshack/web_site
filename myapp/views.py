from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Multimedia
from django.db.models import F
from django.http import HttpResponse
# Create your views here.


class MultimediaViews(TemplateView):
    def get(self, request):
        context = {}
        clay = Multimedia.objects.all()
        context['temp'] = clay
        return render(request, 'home.html', {'temp': clay})


class InfoPageView(TemplateView):
    def get(self, request):
        themes = request.GET.get('themes')
        if themes is None:
            themes = 1
        context = {}
        context['data'] = Multimedia.objects.filter(id=themes)
        return render(request, 'info.html', context)


class EnUzRuViews(ListView):
    template_name = 'en_uz_ru.html'
    def get(self):
        try:
            lang = self.request.session['lang']
        except:
            lang = 'uz'
        queryset = Multimedia.objects.all().values('name_' + lang, 'description_' + lang).annotate(
            name=F('name_' + lang), description=F('description_' + lang))
        return queryset


def setLanguage(request, lang):
    try:
        request.session['lang'] = lang
        return HttpResponse('ok');
    except:
        return HttpResponse('error');