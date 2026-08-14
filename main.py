import parsers
from expense_tracker import ExpenseTracker

if __name__ == "__main__":
    cli = parsers.parse_args()
    expense_tracker = ExpenseTracker()
    match cli["command"]:
        case "add":
            expense_tracker.add_expense(cli["description"], cli["amount"])
        case "update":
            expense_tracker.update_expense(cli["id"], cli["description"], cli["amount"])
        case "delete":
            expense_tracker.delete_expense(cli["id"])
        case "summary":
            expense_tracker.summary_expenses(cli["month"])
        case "list":
            expense_tracker.list_expenses()
        case _:
            print("No command was found")
