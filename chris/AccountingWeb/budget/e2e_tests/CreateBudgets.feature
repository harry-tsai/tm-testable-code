Feature: CreateBudgets
    In order to manage budget of department
    As a department manager
    I want to set budget amount of specific year month

Scenario: create a budget
    Given budget for setting YearMonth <YearMonth> and Amount <Amount>
        | YearMonth | Amount |
        | 202003    | 31     |
    When I create
    Then it should be created successfully

