import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def check_inactivity(self, threshold_days=2):  
        today = datetime.date.today()
        if self.last_entry_date is None:
            print(" 아직 지출 기록이 없습니다. 첫 지출을 입력해보세요!\n")
            return
        days_inactive = (today - self.last_entry_date).days
        if days_inactive >= threshold_days:
            print(f" {days_inactive}일째 지출 기록이 없습니다. 오늘 지출이 있다면 기록해보세요!\n")    


