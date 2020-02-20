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

from .views import budget_create, budget_query_result
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


class BudgetQueryTestCase(unittest.TestCase):
    def setUp(self):        
        self.budget = BudgetsFactory.build()
        self.budget.__class__.objects.all().delete()
        
    def test_empty_budget(self):
        self.request = FakeRequestFactory(POST={'start_date': '20201201', 'end_date': '20201231'})
        self.assertEquals(b"<span id='amount'>0.00</span>\n", budget_query_result(self.request, self.budget).content)


    def test_full_month_budget(self):
        self.budget = BudgetsFactory.build(year_month='202001', budget_money=310)
        self.budget.save()
        self.request = FakeRequestFactory(POST={'start_date': '20200101', 'end_date': '20200131'})
        self.assertEquals(b"<span id='amount'>310.00</span>\n", budget_query_result(self.request, self.budget).content)

    def test_partial_month_budget(self):
        self.budget = BudgetsFactory.build(year_month='202001', budget_money=310)
        self.budget.save()
        self.request = FakeRequestFactory(POST={'start_date': '20200101', 'end_date': '20200130'})
        self.assertEquals(b"<span id='amount'>300.00</span>\n", budget_query_result(self.request, self.budget).content)

    def test_cross_month_budget(self):
        self.budget = BudgetsFactory.build(year_month='202004', budget_money=30)
        self.budget.save()
        self.budget = BudgetsFactory.build(year_month='202005', budget_money=310)
        self.budget.save()
        
        self.request = FakeRequestFactory(POST={'start_date': '20200430', 'end_date': '20200504'})
        self.assertEquals(b"<span id='amount'>41.00</span>\n", budget_query_result(self.request, self.budget).content)

    def test_two_full_months_budget(self):
        self.budget = BudgetsFactory.build(year_month='202006', budget_money=30)
        self.budget.save()
        self.budget = BudgetsFactory.build(year_month='202007', budget_money=310)
        self.budget.save()
        
        self.request = FakeRequestFactory(POST={'start_date': '20200601', 'end_date': '20200731'})
        self.assertEquals(b"<span id='amount'>340.00</span>\n", budget_query_result(self.request, self.budget).content)
        
    def test_one_half_months_budget(self):
        self.budget = BudgetsFactory.build(year_month='202008', budget_money=31)
        self.budget.save()
        self.budget = BudgetsFactory.build(year_month='202009', budget_money=300)
        self.budget.save()
        
        self.request = FakeRequestFactory(POST={'start_date': '20200801', 'end_date': '20200915'})
        self.assertEquals(b"<span id='amount'>181.00</span>\n", budget_query_result(self.request, self.budget).content)
