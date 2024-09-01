from rest_framework import serializers
from image_app.serializers import ImageSerializer
from catalog_app.models import Good


class ManufacturerSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)


class CategorySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    # parent_id = serializers.UUIDField()


class Submenu3Serializer(serializers.Serializer):
    category = CategorySerializer()


class Submenu2Serializer(serializers.Serializer):
    category = CategorySerializer()
    items = Submenu3Serializer(
        required=False, allow_null=True, many=True, read_only=True
    )


class Submenu1Serializer(serializers.Serializer):
    category = CategorySerializer()
    items = Submenu2Serializer(
        required=False, allow_null=True, many=True, read_only=True
    )


class GoodsImageSerializer(serializers.Serializer):
    image = ImageSerializer(required=False, allow_null=True)


class GoodSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    art = serializers.CharField(max_length=50, required=False, allow_blank=True)
    code = serializers.CharField(max_length=11, required=False, allow_blank=True)
    balance = serializers.DecimalField(max_digits=15, decimal_places=3, required=False)
    price = serializers.DecimalField(max_digits=15, decimal_places=2, required=False)
    manufacturer = ManufacturerSerializer(required=False, allow_null=True)
    category = CategorySerializer(required=False, allow_null=True)
    preview = ImageSerializer(
        required=False, allow_null=True, source="image", read_only=True
    )
    images = GoodsImageSerializer(
        required=False, allow_null=True, many=True, read_only=True
    )
    description = serializers.CharField(
        max_length=1024, required=False, allow_blank=True
    )

    def create(self, validated_data):
        good, _ = Good.objects.get_or_create(id=validated_data.get("id"))
        good.name = validated_data.get("id", good.name)
        good.art = validated_data.get("art", good.art)
        good.code = validated_data.get("code", good.code)
        good.balance = validated_data.get("balance", good.balance)
        good.price = validated_data.get("price", good.price)
        good.description = validated_data.get("description", good.description)
        good.save()
        return good


class SimpleGoodSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    art = serializers.CharField(max_length=50, required=False, allow_blank=True)
    code = serializers.CharField(max_length=11, required=False, allow_blank=True)
    balance = serializers.DecimalField(max_digits=15, decimal_places=3, required=False)
    price = serializers.DecimalField(max_digits=15, decimal_places=2, required=False)
    manufacturer_id = serializers.UUIDField(required=False, allow_null=True)
    category_id = serializers.UUIDField(required=False, allow_null=True)
    preview = ImageSerializer(
        required=False, allow_null=True, source="image", read_only=True
    )
    images = GoodsImageSerializer(
        required=False, allow_null=True, many=True, read_only=True
    )
    description = serializers.CharField(
        max_length=1024, required=False, allow_blank=True
    )
