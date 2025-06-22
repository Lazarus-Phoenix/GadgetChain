from rest_framework import serializers
from .models import Network, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NetworkSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    level = serializers.CharField(source='get_level_display', read_only=True)

    class Meta:
        model = Network
        fields = '__all__'
        read_only_fields = ('debt', 'creation_time', 'level')


class NetworkCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = '__all__'
        read_only_fields = ('debt', 'creation_time', 'level')