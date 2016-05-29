from wb_standardizer import *
from ratings_standardizer import *
from filemerger import *

wb = WBStandardizer()

inflation_input = "data/originals/inflation-gdp-percentage.csv"
inflation_output = "data/output/inflation-gdp-percentage.csv"

debt_input = "data/originals/debt-gdp-percentage.csv"
debt_output = "data/output/debt-gdp-percentage.csv"

wb.standardize_tables(inflation_input, inflation_output)
wb.standardize_tables(debt_input, debt_output)

rating = RatingsStandardizer()

credit_input = 'data/originals/credit-ratings-3-2013.csv'
credit_output = 'data/output/credit-ratings-3-2013.csv'

rating.standardize_tables(credit_input, credit_output)

print "Success"

mymerger = CSVMerger()
mymerger.get12and13(credit_output, inflation_output, debt_output)
