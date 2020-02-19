from django.db import models

# Create your models here.
from django.db import models


class Budgets(models.Model):
    year_month = models.CharField(max_length=6)
    budget_money = models.IntegerField()

    class Meta:
        abstract = True
