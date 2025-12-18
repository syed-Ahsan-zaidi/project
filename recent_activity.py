from services.transaction_service import get_recent_transactions

def recent_activity():
    transactions = get_recent_transactions()

    print("Recent Activity")
    print("-" * 40)

    for tx in transactions:
        print(f"{tx.type.upper():6} | ${tx.amount:<8} | {tx.date}")
