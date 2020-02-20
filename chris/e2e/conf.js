exports.config = {
  //自動幫忙啟動 Selenium Server 
  directConnect: true,


  // 設定啟用的 webdriver
  capabilities: {
    'browserName': 'chrome'
  },


  // 設定使用的 testing framework
  framework: 'jasmine',


  // 指定要跑的 test file
  specs: ['query_budget_spec.js'],



  // 啟用 ES7 async, await 非同步語法糖
  // 代表 protractor 不會再幫你 handle promise
  // 需自行處理非同步方法
  SELENIUM_PROMISE_MANAGER: true,

  // Options to be passed to Jasmine.
  jasmineNodeOpts: {
    defaultTimeoutInterval: 30000
  }
};