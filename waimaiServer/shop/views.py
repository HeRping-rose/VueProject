
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status   
from django.shortcuts import render, get_object_or_404
from .models import Shop, Food, ShopCategory
from .serializers import ShopSerializer, FoodSerializer
from .serializers import ShopDetailSerializer
from .serializers import ShopCategorySerializer, ShopCategoryDetailSerializer

# Create your views here.

# 店铺视图
class ShopView(APIView):
    def get(self, request):
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response({
            "code": "1",
            "msg": "成功",
            "data": serializer.data
        })
    def post(self, request):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# 食品视图
class FoodView(APIView):
    def get(self, request):
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# 店铺详情视图
class ShopDetailView(APIView):
    def get(self, request, pk):
        shop = get_object_or_404(Shop, pk=pk)
        serializer = ShopDetailSerializer(shop)
        return Response(serializer.data)
    def put(self, request, pk):
        shop = get_object_or_404(Shop, pk=pk)
        serializer = ShopDetailSerializer(shop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        shop = get_object_or_404(Shop, pk=pk)
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 食品详情视图
class FoodDetailView(APIView):
    def get(self, request, pk):
        food = get_object_or_404(Food, pk=pk)
        serializer = FoodSerializer(food)
        return Response(serializer.data)
    def put(self, request, pk):
        food = get_object_or_404(Food, pk=pk)
        serializer = FoodSerializer(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        food = get_object_or_404(Food, pk=pk)
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 店铺分类视图
class ShopCategoryView(APIView):
    def get(self, request):
        shop_categories = ShopCategory.objects.all()
        serializer = ShopCategorySerializer(shop_categories, many=True)
        return Response({
            "code": "1",
            "msg": "成功",
            "data": serializer.data
        })
    def post(self, request):
        serializer = ShopCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "code": "1",
                "msg": "成功",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(
            {
                "code": "0",
                "msg": "失败",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    # 删除
    def delete(self, request):
        id = request.query_params.get('id')
        ShopCategory.objects.get(id=id).delete()
        return Response({
            "code": "1",
            "msg": "成功",
            "data": "删除成功"
            }, status=status.HTTP_204_NO_CONTENT
        )

# 店铺分类详情视图
class ShopCategoryDetailView(APIView):
    def get(self, request, pk):
        shop_category = ShopCategory.objects.get(pk=pk)
        serializer = ShopCategoryDetailSerializer(shop_category)
        return Response(serializer.data)
    def put(self, request, pk):
        shop_category = ShopCategory.objects.get(pk=pk)
        serializer = ShopCategoryDetailSerializer(shop_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        shop_category = get_object_or_404(ShopCategory, pk=pk)
        shop_category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    