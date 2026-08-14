from dataclasses import asdict, dataclass, field
from datetime import datetime, date
from calendar import month_name
from expense import Expense
import formatters
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
        if not self.ids:
            return 1
        return max(self.ids) + 1

    def calculate_total(self, month: float) -> float:
        total = 0
        with open(self.database, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if (
                    month == 0
                    or datetime.strptime(row["date"], "%Y-%m-%d").month == month
                ):
                    total += float(row["amount"])
        return total

    def add_expense(self, description: str, amount: float):
        id = self.generate_id()
        try:
            new_expense = Expense(id, date.today().isoformat(), description, amount)
        except (ValueError, TypeError) as e:
            print(f"Could not add expense: {e}")
            return
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
        try:
            dummy_expense = Expense(id, date.today().isoformat(), description, amount)
        except (ValueError, TypeError) as e:
            print(f"Could not update expense: {e}")
            return
        for expense in updated_expenses:
            if int(expense["id"]) == id:
                expense["description"] = description
                expense["amount"] = amount
        with open(self.database, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows(updated_expenses)
        print(f"Expense updated successfully (ID: {id})")

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
        try:
            with open(self.database, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, headers)
                writer.writeheader()
                writer.writerows(updated_expenses)
        except OSError as e:
            print(f"Could not save changes: {e}")
            return
        print("Expense deleted successfully")

    def list_expenses(self):
        with open(self.database, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            print(
                f"{headers[0]:<5}{headers[1]:<15}{headers[2]:<15}{headers[3]:<10}".upper()
            )
            for row in reader:
                print(
                    f"{row[headers[0]]:<5}{row[headers[1]]:<15}{row[headers[2]]:<15}${formatters.format_amount(round(row[headers[3]])):<10}"
                )

    def summary_expenses(self, month: int = 0):
        if month < 0 or month > 12:
            print("Month is not a valid value")
            return
        if int(month) != month:
            print("Month must be an Integer")
            return
        total = self.calculate_total(month)
        if month == 0:
            print(f"Total expenses: ${formatters.format_amount(total)}")
        else:
            print(
                f"Total expenses for {month_name[month]}: ${formatters.format_amount(total)}"
            )
