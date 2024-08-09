from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from ..forms import RegistrationForm


class RegisterView(FormView, CreateView):
    template_name = 'users/register.html'
    form_class = RegistrationForm
    success_url = '/'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)

    

    
