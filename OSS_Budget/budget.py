import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        for e in self.expenses:
            if e.description == description:
                print("⚠️ 같은 설명의 지출이 방금 전에 등록되었습니다.")
                choice = input("그래도 추가하시겠습니까? (y/n): ").strip().lower()
                if choice != 'y':
                    print("❌ 지출 추가가 취소되었습니다.\n")
                    return

        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("✅ 지출이 추가되었습니다.\n")
        
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


