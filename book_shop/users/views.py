from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.admin import UserCreationForm


class RegisterView(CreateView):
    """Sign up a new user with :data:`users.admin.UserCreationForm`, then send them to login."""

    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')
