from datetime import date
from models.transaction import Transaction

def get_recent_transactions():
    return [
        Transaction("1", "credit", 250, date(2025, 9, 12)),
        Transaction("2", "debit", 120, date(2025, 9, 11)),
        Transaction("3", "credit", 500, date(2025, 9, 10)),
        Transaction("4", "debit", 80, date(2025, 9, 9)),
        Transaction("5", "credit", 1000, date(2025, 9, 8)),
    ]
