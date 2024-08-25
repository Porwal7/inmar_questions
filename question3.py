# Question #3) Let’s say you have a CSV input file that contains thousands of credit card
# transactions. See sample below:
# Date,Description,TransactionAmount
# 2023-10-01,Fuel,30.0
# 2023-10-10,Fuel,41.0
# 2023-10-31,Fuel,35.0
#
# 3a) Write a simple block of Python code that (a) reads the input file (and all of its transactions)
# and (b) calculates the average transaction amount across all records.


import pandas as pd


def read_csv(csv_path=None):
	path = csv_path if csv_path else "transactions.csv"
	df = pd.read_csv(path)
	return df



def get_avg(pd_df):
	return round(pd_df['TransactionAmount'].mean(), 2)


if __name__ == "__main__":
	transaction_df = read_csv()
	print(get_avg(transaction_df))