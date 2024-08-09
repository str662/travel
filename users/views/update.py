from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from core.custum_permission import LoggedSuperUser

from ..models import ProfileModel
from ..forms import ProfileForm


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView, LoggedSuperUser):
    model = ProfileModel
    form_class = ProfileForm
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user.userprofile
