from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('personal_page/', views.personal_page, name='personal_page'),
    path('register/', views.register, name='register_page'),
    path('login/', views.user_login, name='log_page'),
    path('logout/', views.user_logout, name='logout_page'),
]

#     path('reset_password/', views.PasswordResetView.as_view(), name='password_reset'),
#     path('reset_password/done', views.password_success, name='password_reset_done'),
#     path('reset_password/<uidb64>/<token>', views.PasswordSetView.as_view(), name='password_reset_confirm'),
#     path('reset_password/complete', views.changed_password_message, name='password_reset_complete'),
# ]
