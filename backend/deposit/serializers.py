from rest_framework import serializers
from .models import DepositProduct, DepositOptions, SavingsProduct, SavingsOptions

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'

class DepositProductsSerializer(serializers.ModelSerializer):
    options = DepositOptionsSerializer(many=True, read_only=True)
    
    class Meta:
        model = DepositProduct
        fields = '__all__'

class SavingsOptionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SavingsOptions
        fields = '__all__'

class SavingsProductsSerializer(serializers.ModelSerializer):
    options = SavingsOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = SavingsProduct
        fields = '__all__'
