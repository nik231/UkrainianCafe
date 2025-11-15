from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import RegisterForm


from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from .forms import CustomPasswordResetForm, CustomSetPasswordForm


# Create your views here.


class RegisterView(View):
    template_name = 'app_auth/register.html'
    form_class = RegisterForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="app_photo:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Registration for {username} successful!")
            return redirect(to="app_auth:signin")
        return render(request, self.template_name, {"form": form})


class CustomPasswordResetView(PasswordResetView):
    template_name = 'app_auth/password_reset.html'
    email_template_name = 'app_auth/password_reset_email.html'
    subject_template_name = 'app_auth/password_reset_subject.txt'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('app_auth:password_reset_done')


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'app_auth/password_reset_confirm.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('app_auth:password_reset_complete')
