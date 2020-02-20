const BudgetPageObject = require('./page/budget');

describe('Query empty budget', function() {

    beforeAll(function() {
        browser.waitForAngularEnabled(false);
    });

    it('Go to query budget page', function() {
        BudgetPageObject.goToBudgetPage();
    });

    it('Given start date and end date', function() {
        BudgetPageObject.setStartDateAndEndDate('20201201', '20201231');
    });

    it('When click query button', function() {
        BudgetPageObject.queryBudget();
    });

    it('Then total amount should be ', function() {
        expect(BudgetPageObject.getBudgetResult()).toBe('0');
        browser.sleep(2000);
    });
});


describe('Query partial month budget', function() {
    beforeAll(function() {
        browser.waitForAngularEnabled(false);
    });

    it('Go to query budget page', function() {
      BudgetPageObject.goToBudgetPage();
    });

    it('Given start date and end date', function() {
        BudgetPageObject.setStartDateAndEndDate('20200101', '20200130');
    });

    it('When click query button', function() {
        BudgetPageObject.queryBudget();
    });

    it('Then total amount should be ', function() {
        expect(BudgetPageObject.getBudgetResult()).toBe('300.00');
        browser.sleep(2000);
    });
});

describe('Query full month budget', function() {
    beforeAll(function() {
        browser.waitForAngularEnabled(false);
    });

    it('Go to query budget page', function() {
      BudgetPageObject.goToBudgetPage();
    });

    it('Given start date and end date', function() {
        BudgetPageObject.setStartDateAndEndDate('20200101', '20200131');
    });

    it('When click query button', function() {
        BudgetPageObject.queryBudget();
    });

    it('Then total amount should be ', function() {
        expect(BudgetPageObject.getBudgetResult()).toBe('310.00');
        browser.sleep(2000);
    });
});

describe('Query next moonth budget', function() {
    beforeAll(function() {
        browser.waitForAngularEnabled(false);
    });

    it('Go to query budget page', function() {
      BudgetPageObject.goToBudgetPage();
    });

    it('Given start date and end date', function() {
        BudgetPageObject.setStartDateAndEndDate('20200415', '20200515');
    });

    it('When click query button', function() {
        BudgetPageObject.queryBudget();
    });

    it('Then total amount should be ', function() {
        expect(BudgetPageObject.getBudgetResult()).toBe('51.00');
        browser.sleep(2000);
    });
});