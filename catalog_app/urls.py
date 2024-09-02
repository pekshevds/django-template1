from django.urls import path
from catalog_app.views import (
    ManufacturerView,
    GoodView,
    UpdateCatalogView,
    DataView,
    CategoryView,
)


app_name = "catalog_app"

urlpatterns = [
    path("manufacturer/", ManufacturerView.as_view(), name="manufacturer"),
    path("manufacturer/<str:slug>/", ManufacturerView.as_view(), name="manufacturer"),
    path("category/", CategoryView.as_view(), name="category"),
    path("category/<str:slug>/", CategoryView.as_view(), name="category"),
    path("good/", GoodView.as_view(), name="good"),
    path("good/<str:slug>/", GoodView.as_view(), name="good"),
    path("data/", DataView.as_view(), name="data"),
    path("update-catalog/", UpdateCatalogView.as_view(), name="update-catalog"),
]
