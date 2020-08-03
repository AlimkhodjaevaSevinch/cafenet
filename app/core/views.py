from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.views import View

from app.core.forms import SignUpForm, LogInForm


class MainPageView(TemplateView):
    template_name = 'core/main_page.html'


class SignUpView(FormView):
    template_name = 'core/signup_page.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LogInView(FormView):
    template_name = 'core/login_page.html'
    form_class = LogInForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.cleaned_data.get('user')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, user=user, email=email, password=password)
        login(self.request, user)
        return super().form_valid(form)