from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Budgets

import unittest
import factory
from mock import patch

from django.http import HttpRequest
from django.contrib.auth.models import User
from django.http import Http404

from .views import budget_create
global request, budgets_being_viewed


def FakeRequestFactory(*args, **kwargs):
    budgets = BudgetsFactory()
    request = HttpRequest()
    request.session = kwargs.get('session', {})
    if kwargs.get('POST'):
        request.method = 'POST'
        request.POST = kwargs.get('POST')
    else:
        request.method = 'GET'
        request.POST = kwargs.get('GET', {})
        
        return request

        
class BudgetsFactory(factory.Factory):
    FACTORY_FOR = Budgets
    year_month = factory.Sequence(lambda i: '2020%02d' % (i%12))
    budget_money = factory.Sequence(lambda i: i)


request = FakeRequestFactory()
budgets_being_viewed = BudgetsFactory()
    
    
class BudgetCreateTestCase(unittest.TestCase):
    def test_create_budget(self):
        self.assertEquals(budgets_being_viewed,
                          budget_create(request).get('year_month'))

    def test_update_budget(self):
        self.assertEquals(budgets_being_viewed,
                          budget_create(request).get('year_month'))


