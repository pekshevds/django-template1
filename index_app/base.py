from pytils import translit
import uuid
from django.db import models
from django.utils.dateformat import format


class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.TextField(
        verbose_name="Комментарий", null=False, blank=True, default=""
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True, null=True, blank=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата изменения", auto_now=True, null=True, blank=True
    )
    is_mark = models.BooleanField(verbose_name="Пометка", default=False)

    class Meta:
        abstract = True


class Directory(Base):
    name = models.CharField(
        verbose_name="Наименование",
        max_length=150,
        null=True,
        blank=True,
        default="",
        db_index=True,
    )
    slug = models.SlugField(max_length=300, null=True, blank=True, unique=True)
    is_group = models.BooleanField(verbose_name="Это группа", default=False)

    def __str__(self) -> str:
        return f"{self.name}"

    def save(self) -> None:
        if not self.slug or self.slug == "None":
            self.slug = translit.slugify(self.name)
        return super().save()

    class Meta:
        ordering = ("name",)
        abstract = True


class Document(Base):
    number = models.IntegerField(
        verbose_name="Номер", null=True, blank=True, editable=False, default=0
    )
    date = models.DateTimeField(verbose_name="Дата", null=True, blank=True)

    def __str__(self) -> str:
        return f"Документ №{self.id} от {format(self.date, '%Y.%m.%d')}"

    class Meta:
        abstract = True
