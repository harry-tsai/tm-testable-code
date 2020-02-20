from behave import *

import logging
logger = logging.getLogger(__name__)

@given('budget for setting YearMonth {YearMonth} and Amount {Amount}')
def step_impl(context, YearMonth, Amount):
    context.event["YearMonth"] = YearMonth
    context.event["Amount"] = Amount

@when('when I create')
def step_impl(context):
    url_path = 'http://localhost:8000/budget/budget_create/'
    log.debug("url_path: %s" % url_path)
    log.debug("params: %s" % context.event)
    res = requests.post(
            url_path,
            params=context.event)

    print('res:{}'.format(res))
    context.last_response = res
    
@then('it should be created successfully')
def step_impl(context):
    log.debug("context res status_code: %s" % context.last_response.status_code)
    assert context.last_response.status_code == int(200)

