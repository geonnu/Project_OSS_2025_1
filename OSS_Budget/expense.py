
class Expense:
    def __init__(self, date, category, description, amount, satisfaction):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount
        self.satisfaction = satisfaction  # 1~5점

    def __str__(self):
        return (f"{self.date} | {self.category} | {self.description} | "
                f"{self.amount}원 | 만족도: {self.satisfaction}/5")
