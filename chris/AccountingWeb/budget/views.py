from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from .models import Budgets

def budget(request):
    template = loader.get_template('budget/index.html')
    return HttpResponse(template.render(None, request))

def budget_create(request, budgets=None):
    if budgets is None:
        budgets = Budgets
        
    year_month = request.POST['date']
    budget_money = int(request.POST['budget'])
    print('year_month:{}, budget_money:{}'.format(year_month, budget_money))

    budgets = Budgets.objects.filter(year_month=year_month)
    print('budgets len:{}'.format(len(budgets)))

    if len(budgets) == 0:
        budget = Budgets()
        budget.year_month = year_month
        budget.budget_money = budget_money
        budget.save()
        return HttpResponse("create budget successful")
    else:
        budget = budgets[0]
        budget.budget_money = budget_money
        budget.save()
        return HttpResponse("update budget successful")

