from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from django.views import View

from .forms import UserForm


class IndexView(View):
    template_name = "accounts/index.html"

    def get(self, request):
        return render(request, self.template_name)


class SignUpView(View):
    template_name = "accounts/sign-up.html"

    def get(self, request):
        return render(request, self.template_name, {"form": UserForm()})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(**form.cleaned_data)
                return redirect('accounts:login')
            except IntegrityError as e:
                return render(request, self.template_name, {"form": form, "error": "Username Already Exists"})
        return render(request, self.template_name, {"form": form})


class LoginView(View):
    template_name = "accounts/login.html"

    def get(self, request):
        return render(request, self.template_name, {"form": UserForm()})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user:
                login(request, user)
                return redirect("files:list")
        return render(
            request, self.template_name, {"form": form, "msg": "Invalid details."}
        )
