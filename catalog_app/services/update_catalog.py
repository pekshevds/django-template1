from typing import Any
from django.db import transaction
from catalog_app.models import Good, Category


def handle_parent(data_item: dict[Any, Any] | None) -> Category | None:
    if data_item is None:
        return None
    category, _ = Category.objects.get_or_create(id=data_item.get("id"))
    category.name = data_item.get("name", category.name)
    category.parent = handle_parent(data_item.get("parent"))
    category.save()
    return category


def handle_good(data_item: dict[Any, Any] | None) -> Good | None:
    if data_item is None:
        return None
    good, _ = Good.objects.get_or_create(id=data_item.get("id"))
    for field in "name,code,art,description,balance,price,description".split(","):
        setattr(good, field, data_item.get(field, getattr(good, field)))
    good.category = handle_parent(data_item.get("parent"))
    good.save()
    return good


def update_catalog_from_json(data: list[dict]) -> None:
    with transaction.atomic():
        for data_item in data:
            handle_good(data_item)
