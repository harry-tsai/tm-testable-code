from django.db import models

# Create your models here.
from django.db import models


class Budgets(models.Model):
    year_month = models.CharField(max_length=6, primary_key=True, null=False)
    budget_money = models.IntegerField(null=False)
    objects = models.Manager()
    class Meta:
        abstract = False

    def __str__(self):
        return "year_month=%s budget_money=%s" % (self.year_month, self.budget_money)
