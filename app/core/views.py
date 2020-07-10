from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'core/main_page.html'
