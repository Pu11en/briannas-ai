# main.py

from blockchain_analysis import analyze_transactions
from alert_system import send_alert

def main():
    # Main execution logic
    transactions = analyze_transactions()
    for transaction in transactions:
        if transaction['is_suspicious']:
            send_alert({"transaction_id": transaction['id'], "details": "Suspicious transaction detected"})

if __name__ == "__main__":
    main()
