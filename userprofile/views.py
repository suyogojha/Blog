from django.shortcuts import redirect, render, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserSignupForm
from .forms import forms

# Create your views here.
class Userloginview(LoginView):
    template_name ="login.html"
    redirect_authenticated_user = True
    authentication_form = AuthenticationForm
    
    def get_success_url(self):
        return reverse("blog:home")
    
class UserSignupview(CreateView):
    template_name = "signup.html"
    models = User
    form_class = UserCreationForm
    
    def form_valid(self, form):
        super().form_valid(form)
        user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
        login(self.request, user)
        return redirect(reverse("blog:home"))
                    
    def get_success_url(self):
        return reverse("userprofile:login")
    
    
def user_signup_view(request):
    form = CustomUserSignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
        login(request, user)
        return redirect(reverse("blog:home"))
    return render(request, "signup.html", {"form": form})
                
                
def logout_view(request):
    logout(request)
    return redirect(reverse("blog:home"))