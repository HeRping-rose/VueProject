

from django.urls import path
from .views import (
    ShopView,
    FoodView,
    ShopDetailView,
    FoodDetailView,
    ShopCategoryView,
    ShopCategoryDetailView,
)


urlpatterns = [
    # 店铺分类（兼容旧路由别名）
    path("cate/", ShopCategoryView.as_view(), name="cate"),
    path("categories/", ShopCategoryView.as_view(), name="shop-category-list"),
    path("categories/<int:pk>/", ShopCategoryDetailView.as_view(), name="shop-category-detail"),

    # 店铺
    path("shops/", ShopView.as_view(), name="shop-list"),
    path("shops/<int:pk>/", ShopDetailView.as_view(), name="shop-detail"),

    # 食品
    path("foods/", FoodView.as_view(), name="food-list"),
    path("foods/<int:pk>/", FoodDetailView.as_view(), name="food-detail"),
]