from django.urls import path
from rest_framework.authtoken import views
from api_app.views import index

app_name = "api_app"

urlpatterns = [
    path("", index, name=""),
    path("api-token-auth/", views.obtain_auth_token),
]
