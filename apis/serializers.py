from rest_framework import serializers
from .models import Category, Product, Inquiry

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name','description')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = "__all__"