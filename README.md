

## Simple overview of use/purpose.

## Requirements

 1. Print the total (rate-adjusted) transactional value of each account.
note: to calculate the rate adjusted value of a given transaction, find the rate that was effective on the transaction's book_date and multiply the rate's multiplier by the transaction's value.

2. Find every out of sequence transaction per account.
note: a transaction is out of sequence if its book date is earlier than any preceding transaction when ordered by sequence number

3. Construct a new transaction list where the out-of-sequence transactions are corrected.


## Getting Started

### Dependencies

- Python 3

### Installing
- Move to your target directory, in terminal or via the command prompt.
- Download repo
```sh
git clone git@github.com:diek/parsing_problem.git
```
- Move into parsing_problem/src


### Executing program

- How to run the program
#### Run:
```sh
python app.py
```


## Authors

Derrick Kearney
