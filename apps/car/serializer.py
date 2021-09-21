from rest_framework import serializers

from .models import Brand, Car


class BrandSerializer(serializers.ModelSerializer):
    total_cars = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = ('id', 'name', 'total_cars',)
        read_only_fields = ('id',)

    def get_total_cars(self, obj):
        return obj.cars.count()


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'model', 'brand', 'manufacturing_data',)
        read_only_fields = ('id',)
        extra_kwargs = {
            'manufacturing_data': {'write_only': True}
        }
