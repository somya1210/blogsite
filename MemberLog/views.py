from django.views import generic
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserChangeView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/updateprofile.html'
    success_url = reverse_lazy('home')
    def get_object(self):
        return self.request.user
class PasswordsChangeView(PasswordChangeView):
    template_name='registration/passwordchange.html'
    form_class=PasswordChangeForm
    success_url=reverse_lazy('home')
