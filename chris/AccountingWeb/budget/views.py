from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from .models import Budgets

def budget(request):
    template = loader.get_template('budget/index.html')
    return HttpResponse(template.render(None, request))

def budget_create(request, budgets=None):
    year_month = request.POST['date']
    budget_money = int(request.POST['budget'])
    print('year_month:{}, budget_money:{}'.format(year_month, budget_money))

    if budgets is not None:
        budget_res = budgets.__class__.objects.filter(year_month=year_month)
    else:
        budget_res = Budgets.objects.filter(year_month=year_month)
        
    print('budget_res len:{}'.format(len(budget_res)))

    if len(budget_res) == 0:
        budget = Budgets()
        budget.year_month = year_month
        budget.budget_money = budget_money
        budget.save()
        return HttpResponse("create budget successful")
    else:
        budget = budget_res[0]
        budget.budget_money = budget_money
        budget.save()
        return HttpResponse("update budget successful")

