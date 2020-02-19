describe('budget page', function() {
    beforeAll(async () => {
        browser.waitForAngularEnabled(false);
    });

    it('go to budget page', function() {
      browser.get('http://localhost:8000/budget/');
    });

    it('input budget', function() {
        element(by.id('date')).sendKeys('202002');
        element(by.id('budget')).sendKeys('5000');
        element(by.id('submit')).click();
    });

    it('success', function() {
        const result = element(by.css('body')).getText();
        expect(result).toBe('update budget successful.');
        browser.sleep(2000);
    });
  });


  