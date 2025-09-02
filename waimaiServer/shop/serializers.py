from rest_framework import serializers
from .models import ShopCategory, Shop, Food


class ShopCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopCategory
        fields = [
            'id', 'name', 'description', 'icon', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = [
            'id', 'category', 'name', 'icon', 'phone', 'address',
            'activity', 'business_hours', 'is_open', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'id', 'shop', 'category', 'name', 'image', 'price',
            'purchase_count', 'is_new', 'is_hot', 'description',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'purchase_count', 'created_at', 'updated_at']


# 详情序列化器（嵌套关联合集）
class ShopDetailSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True, read_only=True)

    class Meta:
        model = Shop
        fields = [
            'id', 'category', 'name', 'icon', 'phone', 'address',
            'activity', 'business_hours', 'is_open', 'created_at', 'updated_at',
            'foods'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ShopCategoryDetailSerializer(serializers.ModelSerializer):
    shops = ShopSerializer(many=True, read_only=True)

    class Meta:
        model = ShopCategory
        fields = [
            'id', 'name', 'description', 'icon', 'created_at', 'updated_at',
            'shops'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

