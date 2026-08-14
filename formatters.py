def format_amount(amount: float) -> str:
    if int(amount) == amount:
        return f"{int(amount)}"
    else:
        return f"{amount:.2f}"
