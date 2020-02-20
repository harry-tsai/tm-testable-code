from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from .models import Budgets
from .budget_repo import BudgetRepo
import datetime
from collections import Counter
from calendar import monthrange

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

def daterange(start_date, end_date):
    date_list = list()
    for n in range(int ((end_date - start_date).days)+1):
        date_list.append((start_date + datetime.timedelta(n)).strftime("%Y%m%d"))
    return date_list


def budget_query_result(request, budgets=None):
    start_date_str = request.POST['start_date']
    end_date_str = request.POST['end_date']
    start_datetime = datetime.datetime.strptime(start_date_str, "%Y%m%d")
    end_datetime = datetime.datetime.strptime(end_date_str, "%Y%m%d")
    print('start_date:{}, end_date:{}'.format(start_date_str, end_date_str))
    date_list = daterange(start_datetime, end_datetime)
    print('date_list:{}'.format(date_list))
    #[20200101, 20200102, ...]
    month_list = [date_time[:-2] for date_time in date_list]
    month_list_distinct = set(month_list)
    month_list_collect = Counter(month_list)
    print('month_list_collect:{}'.format(month_list_collect))
    budget_repo = BudgetRepo(budgets)
    budget_res = budget_repo.get_all_objects()
    print('budget_res:{}'.format(budget_res))
    budget_month_list = [res.year_month for res in budget_res]
    print('budget_month_list:{}'.format(budget_month_list))
    total_amount = 0.0
    for query_month in month_list:
        for idx, budget_month in enumerate(budget_month_list):
            days = monthrange(int(budget_month[:4]), int(budget_month[4:6]))[1]
            if query_month == budget_month:
                total_amount += float(budget_res[idx].budget_money)/days
    print('total_amount:{}'.format(total_amount))
    context = {'amount': total_amount}
    return render(request, 'budget/query_result.html', context) 

def budget_query(request):
    template = loader.get_template('budget/query.html')
    return HttpResponse(template.render(None, request))
