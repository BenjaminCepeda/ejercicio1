from django.shortcuts import render

from rest_framework import viewsets
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

from .serializers import CurrenciesSerializer

from .models import Currencies


class CurrenciesViewSet(viewsets.ModelViewSet):
    queryset = Currencies.objects.all().order_by('id')
    serializer_class = CurrenciesSerializer
