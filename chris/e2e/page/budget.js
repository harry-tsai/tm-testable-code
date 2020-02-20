const BudgetPageObject = function() {
    this.goToBudgetPage = () => {
        browser.get('http://localhost:8000/budget/budget_query');
    }

    this.setStartDateAndEndDate = (startDate, endDate) => {
        element(by.name('start_date')).sendKeys(startDate);
        element(by.name('end_date')).sendKeys(endDate);
        element(by.id('query')).click();
    }

    this.queryBudget = () => {
        element(by.id('query')).click();
    }

    this.getBudgetResult = () => {
        return element(by.id('amount')).getText();
    }
};

module.exports = new BudgetPageObject();