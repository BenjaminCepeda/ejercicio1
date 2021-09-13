from django.db import models


class Curencies(models.Model):
    query_date = models.DateTimeField(null=False,verbose_name='QueryDate')
    currency = models.CharField(max_length=3,null=False,verbose_name='currency')
    final_quote = models.FloatField(null=False,verbose_name='final_quote')

    class Meta:
        ordering = ['-query_date', 'currency']