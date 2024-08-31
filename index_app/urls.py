from django.urls import path
from index_app.views import index

app_name = "index_app"

urlpatterns = [
    path("", index, name=""),
]
