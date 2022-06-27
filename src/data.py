'''/*
  transactions stores a list of financial transactions
  each transasction has the following properties":

  - "value:            the dollar "value of the transaction
  - "account_id:       the ID of the "account that the transaction belongs to
  - "book_date:        the date on which the transaction was processes
  - "sequence_number:  informs on the order in which the transactions were processed per-"account

*/'''


TRANSACTIONS = [
  {
    "sequence_number": 5,
    "book_date": "2020-01-05",
    "account_id": 1,
    "value": 202112
  },
  {
    "sequence_number": 4,
    "book_date": "2020-01-02",
    "account_id": 1,
    "value": 90212
  },
  {
    "sequence_number": 3,
    "book_date": "2020-01-02",
    "account_id": 1,
    "value": 150123
  },
  {
    "sequence_number": 2,
    "book_date": "2020-01-03",
    "account_id": 1,
    "value": 88732
  },
  {
    "sequence_number": 1,
    "book_date": "2020-01-01",
    "account_id": 1,
    "value": 242292
  },
  {
    "sequence_number": 3,
    "book_date": "2020-03-02",
    "account_id": 2,
    "value": 192842
  },
  {
    "sequence_number": 2,
    "book_date": "2020-04-03",
    "account_id": 2,
    "value": 142592
  },
  {
    "sequence_number": 1,
    "book_date": "2020-05-01",
    "account_id": 2,
    "value": 222232
  },
  {
    "sequence_number": 4,
    "book_date": "2020-02-02",
    "account_id": 3,
    "value": 212092
  },
  {
    "sequence_number": 3,
    "book_date": "2020-02-28",
    "account_id": 3,
    "value": 202712
  },
  {
    "sequence_number": 2,
    "book_date": "2020-04-03",
    "account_id": 3,
    "value": 202212
  },
  {
    "sequence_number": 1,
    "book_date": "2020-05-01",
    "account_id": 3,
    "value": 209312
  }
]

ACCOUNTS = [
  {
    "id": 1,
    "name": "ACME Co."
  },
  {
    "id": 2,
    "name": "123 LLC."
  },
  {
    "id": 3,
    "home_state": "The Brothers, Warner"
  }
]

'''/*
 * a list of rates used to calculate the rate-adjusted "value of any given transaction
 * - sorted in chronological ascending order
 * - a rate comes into effect on its effective_date and remains in effect until the next
 *   rate's effective_date
 */'''
MONTHLY_RATES = [
  {
    "effective_date": "2020-01-01",
    "multiplier": 0.9
  },
  {
    "effective_date": "2020-02-01",
    "multiplier": 1.3
  },
  {
    "effective_date": "2020-03-03",
    "multiplier": 1.5
  },
  {
    "effective_date": "2020-04-01",
    "multiplier": 1.3
  },
  {
    "effective_date": "2020-05-15",
    "multiplier": 1.5
  },
  {
    "effective_date": "2020-06-01",
    "multiplier": 1.3
  },
  {
    "effective_date": "2020-07-21",
    "multiplier": 1.0
  }
]
