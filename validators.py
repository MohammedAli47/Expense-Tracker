def validate_id(id: int) -> None:
    if not isinstance(id, int):
        raise TypeError("id must be an integer")
    if id < 0:
        raise ValueError("id must be positive")


def validate_date(date: str) -> None:
    if not isinstance(date, str):
        raise TypeError("date must be an string")


def validate_description(description: str) -> None:
    if not isinstance(description, str):
        raise TypeError("description must be a string")
    if len(description) == 0:
        raise ValueError("description must not be a empty")


def validate_amount(amount: float) -> None:
    if not isinstance(amount, float):
        raise TypeError("amount must be a float")
    if amount < 0:
        raise ValueError("amount must be positive")
