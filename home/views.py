from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'home/index.html'
    


class HowItWorks(TemplateView):
    template_name = 'home/how-it-works.html'
