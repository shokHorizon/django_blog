from .forms import RegisterForm
from django.urls import reverse_lazy
from django.views import generic


class UserCreateView(generic.CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy('login')
