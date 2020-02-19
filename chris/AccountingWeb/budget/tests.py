# Create your tests here.
from django.test import TestCase
from . import models

import unittest
import factory
from factory.django import DjangoModelFactory
from mock import patch

from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.http import Http404

from .views import budget_create
import json

def FakeRequestFactory(*args, **kwargs):
    request = HttpRequest()
    request.session = kwargs.get('session', {})
    request.method = 'POST'
    request.POST = kwargs.get('POST')
        
    return request

        
class BudgetsFactory(DjangoModelFactory):
    class Meta:
        model = models.Budgets
        
class BudgetCreateTestCase(unittest.TestCase):
    def setUp(self):
        
        self.budget = BudgetsFactory.build(year_month='202003', budget_money=300)
        self.budget.__class__.objects.all().delete()
        self.budget.save()
        
    def test_create_budget(self):
        self.request = FakeRequestFactory(POST={'date': '202004', 'budget': 400})
        print('budget factory:{}'.format(self.budget))
        self.assertEquals(b'create budget successful', budget_create(self.request, self.budget).content)

    def test_update_budget(self):
        self.request = FakeRequestFactory(POST={'date': '202003', 'budget': 500})
        print('budget factory:{}'.format(self.budget))
        self.assertEquals(b'update budget successful', budget_create(self.request, self.budget).content)


