import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        while True:
            try:
                satisfaction = int(input("이 지출에 대한 만족도를 1~5점으로 입력하세요: "))
                if 1 <= satisfaction <= 5:
                    break
                else:
                    print("1부터 5 사이의 숫자를 입력하세요.")
            except ValueError:
                print("정수로 입력해주세요.")
        expense = Expense(today, category, description, amount, satisfaction)
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
        
    def regret_spending(self):
        low_scores = [e for e in self.expenses if e.satisfaction <= 2]
        if not low_scores:
            print("후회되는 지출이 없습니다.\n")
            return
        print("\n[후회 지출 목록]")
        for e in low_scores:
            print(f"- {e}")
        print()

