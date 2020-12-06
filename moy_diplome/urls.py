from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.shortcuts import redirect
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", include("home.urls")),
    path("workout/", include("workout.urls")),
    path("yoga/", include("yoga.urls")),
    path("accounts/", include("accountes.urls")),
    path("stretching/", include("stretching.urls")),
    path("about_us/", include("about_us.urls")),
    path('i18n/', include('django.conf.urls.i18n')),
    path('account/', include('django.contrib.auth.urls')),

    path("", lambda request: redirect("/home/")),
]

# urlpatterns += i18n_patterns(
#     path('accounts/', include('allauth.urls')),
# )

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("home/", include("home.urls")),
#     path("", lambda request: redirect("/home/")),
#     url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
# ]



# if settings.DEBUG == True:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)