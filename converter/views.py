from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
import requests
import json
from .serializers import CurrenciesSerializer

from .models import Currencies
import logging


class CurrenciesViewSet(viewsets.ModelViewSet):
    webhook_url = 'https://webhook.site/4ed54cff-41ba-423e-9f46' \
                  '-b2c87408daf9 '
    filter_backends = (SearchFilter,)
    queryset = Currencies.objects.all().order_by('id')
    serializer_class = CurrenciesSerializer
    search_fields = ('currency', 'query_date', )

    def get_queryset(self):
        serializer = self.get_serializer(self.queryset, many=True)
        requests.post(self.webhook_url, data=json.dumps(serializer.data),
                      headers={'Content-Type': 'application/json'})
        return self.queryset
    """
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        requests.post(self.webhook_url, data=json.dumps(serializer.data),
                      headers={'Content-Type': 'application/json'})
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        # do your customization here
        query_set = self.get_queryset()
        serializer = self.get_serializer(query_set, many=True)
        requests.post(self.webhook_url, data=json.dumps(serializer.data),
                      headers={'Content-Type': 'application/json'})
        return Response(serializer.data)
    """