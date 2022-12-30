from django.urls import path, include

urlpatterns = [
    path("registration/", include("dj_rest_auth.registration.urls")),
    path("auth/", include("dj_rest_auth.urls")),
]
