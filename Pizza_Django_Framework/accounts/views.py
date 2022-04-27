from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView

from Pizza_Django_Framework.accounts.forms import LoginForm, RegisterForm, ProfileForm
from Pizza_Django_Framework.accounts.models import Profile
from Pizza_Django_Framework.pizza.models import Pizza


class LoginUserView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm
    success_url = reverse_lazy('home')


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result


def logout_user(request):
    logout(request)
    return redirect('home')


class ProfileDetailsView(LoginRequiredMixin, FormView):
    template_name = 'accounts/user_profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profile details')
    object = None

    def get(self, request, *args, **kwargs):
        self.object = Profile.objects.get(pk=request.user.id)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = Profile.objects.get(pk=request.user.id)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object.profile_image = form.cleaned_data['profile_image']
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user_pizzas'] = Pizza.objects.filter(user_id=self.request.user.id)
        context['profile'] = self.object

        return context