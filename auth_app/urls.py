from django.urls import path
from auth_app.views import index

app_name = "auth_app"

urlpatterns = [
    path("", index, name=""),
]
