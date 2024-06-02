from rest_framework import serializers
from .models import DepositProduct, DepositOptions

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):
    product = DepositProductsSerializer(read_only=True)
    
    class Meta:
        model = DepositOptions
        fields = '__all__'