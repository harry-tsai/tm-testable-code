from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from .models import Budgets

def budget(request):
    template = loader.get_template('budget/index.html')
    return HttpResponse(template.render(None, request))

def budget_create(request):
    year_month = request.POST['date']
    budget_money = int(request.POST['budget'])

    try:
        budget = Budgets.objects.get(year_month=year_month)
        budget.money = budget_money
        budget.save()
        return HttpResponse("update budget successful.")
    except:
        budget = Budgets()
        budget.year_month = year_month
        budget.budget_money = budget_money
        budget.save()
        return HttpResponse("create budget successful.")
