const BudgetPageObject = require('./page/budget');

//載入 sqlite3
const sqlite3 = require("sqlite3").verbose();
//新增一個sqlite3的資料庫test.db
var db = new sqlite3.Database('../AccountingWeb/db.sqlite3');

describe('Query empty budget', function() {

    beforeAll(function() {
        browser.waitForAngularEnabled(false);
        db.serialize(function() {
            //刪除資料
            var sql04 = "delete from budget_Budgets";
            db.run(sql04);
        });
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
        expect(BudgetPageObject.getBudgetResult()).toBe('0.00');
        browser.sleep(2000);
    });
});


describe('Query partial month budget', function() {
    beforeAll(function() {
        browser.waitForAngularEnabled(false);
        db.serialize(function() {
            //刪除資料
            var sql04 = "delete from budget_Budgets";
            db.run(sql04);  
            sql04 = "INSERT INTO budget_Budgets(year_month, budget_money) VALUES ('202001','310');";
            db.run(sql04);  
        });
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
        db.serialize(function() {
            //刪除資料
            var sql04 = "delete from budget_Budgets";
            db.run(sql04);  
            sql04 = "INSERT INTO budget_Budgets(year_month, budget_money) VALUES ('202001','310');";
            db.run(sql04);  
        });
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

describe('Query cross moonth budget', function() {
    beforeAll(function() {
        browser.waitForAngularEnabled(false);
        db.serialize(function() {
            //刪除資料
            var sql04 = "delete from budget_Budgets";
            db.run(sql04);  
            sql04 = "INSERT INTO budget_Budgets(year_month, budget_money) VALUES ('202004','30');";
            db.run(sql04);  
            sql04 = "INSERT INTO budget_Budgets(year_month, budget_money) VALUES ('202005','310');";
            db.run(sql04);  
        });
    });

    it('Go to query budget page', function() {
      BudgetPageObject.goToBudgetPage();
    });

    it('Given start date and end date', function() {
        BudgetPageObject.setStartDateAndEndDate('20200430', '20200504');
    });

    it('When click query button', function() {
        BudgetPageObject.queryBudget();
    });

    it('Then total amount should be ', function() {
        expect(BudgetPageObject.getBudgetResult()).toBe('41.00');
        browser.sleep(2000);
    });
});