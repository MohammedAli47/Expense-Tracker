from dataclasses import dataclass
import validators


@dataclass
class Expense:
    id: int
    date: str
    description: str
    amount: float

    def __post_init__(self):
        validators.validate_id(self.id)
        validators.validate_date(self.date)
        validators.validate_description(self.description)
        validators.validate_amount(self.amount)
