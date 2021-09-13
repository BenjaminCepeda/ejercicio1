from rest_framework import serializers
from .models import Currencies


class CurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = ['id', 'query_date', 'currency', 'final_quote']
        extra_kwargs = {'id': {'required': False}}
