from .models import Budgets

class BudgetRepo:
    def __init__(self, budgets):
        if budgets is not None:
            self.budget = budgets.__class__.objects
        else:
            self.budget = Budgets.objects
        
    def get_all_objects(self):
        return self.budget.all()
