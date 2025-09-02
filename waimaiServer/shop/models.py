from django.db import models

# Create your models here.

class ShopCategory(models.Model):
    """店铺分类模型"""
    name = models.CharField(max_length=100, verbose_name='分类名称')
    description = models.TextField(blank=True, null=True, verbose_name='分类描述')
    icon = models.ImageField(upload_to='category_icons/', blank=True, null=True, verbose_name='分类图标')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '店铺分类'
        verbose_name_plural = '店铺分类'
        ordering = ['name']

    def __str__(self):
        return self.name


class Shop(models.Model):
    """店铺模型"""
    category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE, related_name='shops', verbose_name='店铺分类')
    name = models.CharField(max_length=200, verbose_name='店铺名称')
    icon = models.ImageField(upload_to='shop_icons/', blank=True, null=True, verbose_name='店铺图标')
    phone = models.CharField(max_length=20, verbose_name='店铺电话')
    address = models.TextField(verbose_name='店铺地址')
    activity = models.TextField(blank=True, null=True, verbose_name='店铺活动')
    business_hours = models.CharField(max_length=100, verbose_name='营业时间')
    is_open = models.BooleanField(default=True, verbose_name='是否营业')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '店铺'
        verbose_name_plural = '店铺'
        ordering = ['name']

    def __str__(self):
        return self.name


class Food(models.Model):
    """食品模型"""
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='foods', verbose_name='所属店铺')
    category = models.CharField(max_length=100, verbose_name='食品分类')
    name = models.CharField(max_length=200, verbose_name='食品名称')
    image = models.ImageField(upload_to='food_images/', blank=True, null=True, verbose_name='食品图片')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='食品价格')
    purchase_count = models.IntegerField(default=0, verbose_name='购买数量')
    is_new = models.BooleanField(default=False, verbose_name='是否新品')
    is_hot = models.BooleanField(default=False, verbose_name='是否热门')
    description = models.TextField(blank=True, null=True, verbose_name='食品描述')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '食品'
        verbose_name_plural = '食品'
        ordering = ['name']

    def __str__(self):
        return self.name
