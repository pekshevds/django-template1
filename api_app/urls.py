from django.urls import path, include
from rest_framework.authtoken import views


app_name = "api_app"

urlpatterns = [
    path("user/", include("auth_app.urls", namespace="auth_app")),
    path("catalog/", include("catalog_app.urls", namespace="catalog_app")),
    path("api-token-auth/", views.obtain_auth_token),
]
