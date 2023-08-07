from django.urls import path
from .views import ShowProfilePage

urlpatterns = [
    path("profilepage/<int:pk>/", ShowProfilePage.as_view(), name = "profilepage")
]