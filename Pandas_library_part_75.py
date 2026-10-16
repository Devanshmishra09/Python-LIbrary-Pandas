# Program 5: Bank Transaction Audit and Balance Calculator
# Description: Processes account deposits/withdrawals and audits balances.

import pandas as pd


def create_transaction_log():
    """Generates bank transaction entries."""
    transactions = {
        "Txn_ID": ["T1001", "T1002", "T1003", "T1004", "T1005", "T1006", "T1007", "T1008"],
        "Acc_No": ["ACC501", "ACC502", "ACC501", "ACC503", "ACC502", "ACC504", "ACC501", "ACC503"],
        "Customer": ["Rahul", "Ananya", "Rahul", "Deepak", "Ananya", "Simran", "Rahul", "Deepak"],
        "Txn_Type": ["Credit", "Credit", "Debit", "Credit", "Debit", "Credit", "Credit", "Debit"],
        "Amount": [15000, 25000, 5000, 18000, 8000, 30000, 12000, 22000],
    }
    return pd.DataFrame(transactions)


def audit_account_balances(df):
    """Computes signed transaction impacts and sums account balances."""
    df["Signed_Amount"] = df.apply(
        lambda r: r["Amount"] if r["Txn_Type"] == "Credit" else -r["Amount"],
        axis=1,
    )

    balance_summary = (
        df.groupby(["Acc_No", "Customer"])
        .agg(
            Total_Credits=("Amount", lambda x: x[df.loc[x.index, "Txn_Type"] == "Credit"].sum()),
            Total_Debits=("Amount", lambda x: x[df.loc[x.index, "Txn_Type"] == "Debit"].sum()),
            Net_Balance=("Signed_Amount", "sum"),
        )
        .reset_index()
    )

    balance_summary["Account_Status"] = balance_summary["Net_Balance"].apply(
        lambda b: "Healthy" if b >= 10000 else "Low Balance"
    )
    return df, balance_summary


def display_audit_report(tx_df, balance_df):
    """Outputs audit logs and summary statements."""
    print("=== TRANSACTION LEDGER ===")
    print(tx_df[["Txn_ID", "Acc_No", "Customer", "Txn_Type", "Amount"]].to_string(index=False))
    print("\n" + "=" * 45)
    print("=== CUSTOMER ACCOUNT BALANCES ===")
    print(balance_df.to_string(index=False))


def main():
    raw_tx = create_transaction_log()
    _, summary = audit_account_balances(raw_tx)
    display_audit_report(raw_tx, summary)


if __name__ == "__main__":
    main()
