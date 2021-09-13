from django.db import models


class Currencies(models.Model):
    query_date = models.DateTimeField(null=False,verbose_name='QueryDate')
    currency = models.CharField(max_length=10,null=False,verbose_name='currency')
    final_quote = models.FloatField(null=False,verbose_name='final_quote')

    class Meta:
        ordering = ['-query_date', 'currency']