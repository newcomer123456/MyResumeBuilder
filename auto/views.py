from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from auto.models import CustomUser
from django.views.generic import FormView, DetailView, View
from auto import models
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm, SignupForm, CustomUserUpdateForm, CustomUserDetailForm
from django import forms
from .mixins import IsOwnerOrAdminMixin
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class SignupView(View):
    template_name = 'auto/signup.html'
    form_class = SignupForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            foto = forms.ImageField(required=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            print(user.foto)
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('detail-user', pk=user.pk)

        return render(request, self.template_name, {'form': form})

class LoginView(View):
    template_name = 'auto/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('detail-user', pk=user.pk)
            else:
                form.add_error(None, 'Invalid username or password')
        return render(request, self.template_name, {'form': form})

class UserDetailView(DetailView):
    model = models.CustomUser
    template_name = "auto/detail_user.html"
    form_class = CustomUserDetailForm
    success_url = reverse_lazy("detail-user")

class HomepageTemplateView(TemplateView):
    template_name = "auto/homepage.html"

class CustomLogoutView(LogoutView):
    next_page='login'

class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "auto/update_user.html"
    form_class = CustomUserUpdateForm
    success_url = reverse_lazy("detail-user")

    def get(self, request, pk):
        user = request.user
        form = self.form_class(instance = user)
        return render(request, self.template_name, {'form':form, 'user':user})
    
    def post(self, request, pk):
        user = request.user
        form = self.form_class(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            return redirect('detail-user', pk=user.id)
        return render(request, self.template_name, {'form': form, 'user':user})

class UserDeleteView(LoginRequiredMixin, View):
    template_name = "auto/delete_user.html"

    def get(self, request, pk):
        return render(request, self.template_name, {'user': request.user})

    def post(self, request, pk):
        user = CustomUser.objects.get(pk=request.user.id)
        user.delete()
        return redirect('homepage') 