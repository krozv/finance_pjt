from rest_framework import serializers
from .models import DepositProduct, DepositOptions, SavingsProduct, SavingsOptions

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):
    product = DepositProductsSerializer(read_only=True)
    
    class Meta:
        model = DepositOptions
        fields = '__all__'

class SavingsProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsProduct
        fields = '__all__'

class SavingsOptionsSerializer(serializers.ModelSerializer):
    product = SavingsProductsSerializer(read_only=True)
    
    class Meta:
        model = SavingsOptions
        fields = '__all__'