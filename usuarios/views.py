from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class IndexTemplate(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('account_login')
    template_name = 'index.html'