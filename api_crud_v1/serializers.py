from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from api_crud_v1.models import Product


class ProductModelSerializer(ModelSerializer):

    def validate_price(self, value):
        if value <= 0:
            raise ValidationError("Price must be greater than 0")
        return value

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']
