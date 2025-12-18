from dataclasses import dataclass
from datetime import date
from typing import Literal

@dataclass
class Transaction:
    id: str
    type: Literal["credit", "debit"]
    amount: float
    date: date
