from collections import defaultdict

from data import ACCOUNTS, MONTHLY_RATES, TRANSACTIONS


def get_account_name(id):
    for account in ACCOUNTS:
        # catch inconsistent account naming property
        if account["id"] == id and id == 3:
            return account["home_state"]
        if account["id"] == id:
            return account["name"]
    return 0


def get_multiplier_for_date(rate_date):
    multiplier = None

    for rate in MONTHLY_RATES:
        if rate_date >= rate["effective_date"]:
            return rate["multiplier"]

    if multiplier is None:
        raise Exception("Could not find multiplier (bad data?)")


def calculate_rate_adjustment(transactions):
    total = 0
    for t in transactions:
        multiplier = get_multiplier_for_date(t["book_date"])
        total += t["value"] * multiplier

    return total


def find_out_of_sequence_transactions(transactions):
    if not transactions:
        return []

    problems = []
    current = transactions[0]["book_date"]

    for transaction in transactions[1:]:
        if transaction["book_date"] < current:
            problems.append(transaction)
        else:
            current = transaction["book_date"]

    return problems


def correct_not_sequential(transactions):
    transactions.sort(key=lambda transaction: transaction["book_date"])
    for sequence_number, transaction in enumerate(transactions, 1):
        transaction["sequence_number"] = sequence_number


def main():
    transactions_by_account = defaultdict(list)

    for transaction in TRANSACTIONS:
        transactions_by_account[transaction["account_id"]].append(transaction)

    for transactions in transactions_by_account.values():
        transactions.sort(key=lambda transaction: transaction["sequence_number"])

    print("Step 1 ====== Total (rate-adjusted) transactional value of each account\n")
    for account in ACCOUNTS:
        name = get_account_name(account["id"])
        total = calculate_rate_adjustment(transactions_by_account[account["id"]])
        print(f"{name}: ${total:.2f}")

    print("\nStep 2 ====== Find every out of sequence transaction per account\n")
    for account in ACCOUNTS:
        name = get_account_name(account["id"])
        transactions = transactions_by_account[account["id"]]
        problems = find_out_of_sequence_transactions(transactions)
        if problems:
            print(f"{name} has the following transactions:")
            print("sequence no.  book_date")
            for transaction in transactions:
                print(
                    f"   {transaction['sequence_number']}          {transaction['book_date']} "
                )

            print(f"{name} has the following problems:")
            print("sequence no.  book_date")
            for problem in problems:
                print(
                    f"   {problem['sequence_number']}          {problem['book_date']} "
                )
            print("\n")

    print(
        "Step 3 ====== Construct a new transaction list where the out-of-sequence "
        "transactions are corrected.\n"
    )
    for account in ACCOUNTS:
        name = get_account_name(account["id"])
        transactions = transactions_by_account[account["id"]]
        correct_not_sequential(transactions)

        print(f"{name} has the following transactions after changing sequence numbers:")
        print("sequence no.  book_date")
        for transaction in transactions:
            print(
                f"   {transaction['sequence_number']}          {transaction['book_date']} "
            )
        print()


if __name__ == "__main__":
    main()
