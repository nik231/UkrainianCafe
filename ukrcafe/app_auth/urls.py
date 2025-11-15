from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views


app_name = "app_auth"

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(template_name='app_auth/login.html', form_class=LoginForm, redirect_authenticated_user=True), name='signin'),
    path('logout/', LogoutView.as_view(template_name='app_auth/logout.html'), name='logout'),
    path('password-reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(
        template_name='app_auth/password_reset_done.html'
    ), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset-complete/', views.PasswordResetCompleteView.as_view(
        template_name='app_auth/password_reset_complete.html'
    ), name='password_reset_complete')
]
