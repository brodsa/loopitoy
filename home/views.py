from django.views.generic import TemplateView


class Index(TemplateView):
    """A view to render home page"""
    template_name = 'home/index.html'
    


class HowItWorks(TemplateView):
    """A view to render how it works page"""
    template_name = 'home/how-it-works.html'


class PrivacyPolicy(TemplateView):
    """A view to render privac policy"""
    template_name = 'home/privacy-policy.html'
