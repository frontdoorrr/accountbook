from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"log", views.AccountDetailViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
