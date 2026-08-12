from dataclasses import asdict, dataclass, field
from datetime import datetime, date
from calendar import month_name
from expense import Expense
import csv

headers = ["id", "date", "description", "amount"]


@dataclass
class ExpenseTracker:
    database: str = "expenses.csv"
    ids: list[int] = field(default_factory=list)

    def __post_init__(self):
        try:
            with open(self.database, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.ids.append(int(row["id"]))
        except FileNotFoundError:
            # If file doesn't exist, create it
            with open(self.database, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, headers)
                writer.writeheader()

    def generate_id(self) -> int:
        new_id = 1
        while new_id in self.ids:
            new_id += 1
        return new_id

    def add_expense(self, description: str, amount: float):
        id = self.generate_id()
        new_expense = Expense(id, date.today().isoformat(), description, amount)
        with open(self.database, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, headers)
            writer.writerow(asdict(new_expense))
        print(f"Expense added successfully (ID: {id})")

    def update_expense(self, id: int, description: str, amount: float):
        if id not in self.ids:
            print(f"No Expense with ID: {id}")
            return
        updated_expenses = []
        with open(self.database, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                updated_expenses.append(row)
        for expense in updated_expenses:
            if int(expense["id"]) == id:
                expense["description"] = description
                expense["amount"] = amount
        with open(self.database, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows(updated_expenses)

    def delete_expense(self, id: int):
        if id not in self.ids:
            print(f"No Expense with ID: {id}")
            return
        updated_expenses = []
        with open(self.database, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                updated_expenses.append(row)
        for expense in updated_expenses:
            if int(expense["id"]) == id:
                updated_expenses.remove(expense)
        with open(self.database, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows(updated_expenses)
        print("Expense deleted successfully")

    def list_expenses(self):
        with open(self.database, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            print(
                f"{headers[0]:<5}{headers[1]:<15}{headers[2]:<15}{headers[3]:<10}".upper()
            )
            for row in reader:
                print(
                    f"{row[headers[0]]:<5}{row[headers[1]]:<15}{row[headers[2]]:<15}{row[headers[3]]:<10}"
                )

    def summary_expenses(self, month: int = 0):
        if month < 0 or month > 12:
            print("Month is not a valid value")
            return
        if int(month) != month:
            print("Month must be an Integer")
            return
        total = 0
        with open(self.database, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            if month == 0:
                for row in reader:
                    total += float(row["amount"])
                print(f"Total Expenses: ${total}")
            else:
                for row in reader:
                    if datetime.strptime(row["date"], "%Y-%m-%d").month == month:
                        total += float(row["amount"])
                print(f"Total Expenses for {month_name[month]}: ${total}")
