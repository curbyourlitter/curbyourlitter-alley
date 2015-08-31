from django.db import models


class SocrataResource(models.Model):
    conditions = models.TextField()
    domain = models.CharField(max_length=100)
    endpoint = models.CharField(max_length=500)
    token = models.CharField(max_length=50)
    unique_key = models.CharField(max_length=50)

    def __str__(self):
        return '{}{}'.format(self.domain, self.endpoint)


class CartodbTable(models.Model):
    apiKey = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    table = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.table)


class Connection(models.Model):
    cartodb_table = models.ForeignKey('CartodbTable')
    socrata_resource = models.ForeignKey('SocrataResource')
    adapter = models.CharField(max_length=50, blank=True, null=True)

    def get_adapter(self):
        from . import adapters
        return getattr(adapters, self.adapter)

    def __str__(self):
        return '{} -> {}'.format(self.socrata_resource, self.cartodb_table)
