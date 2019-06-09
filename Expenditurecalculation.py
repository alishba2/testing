#Calculation company's Expenditure

#Workers Expenditure
def expenditure_of_worker():
    salary = (50000 + 35000 + 15000 + 10000 + 10000 + 10000 + 10000 + 10000 + 10000 + 10000 + 10000 + 10000 )
    return salary

Salaryofworkers = expenditure_of_worker()

#Company Expenditure per month
Rent = 60000
GeneralExpenditures = 20000
companyExpenditure = Rent + GeneralExpenditures

# Total Expenditures per month
Total = Salaryofworkers + companyExpenditure
print(" Company's Monthly Expenditure is " , Total)

# Total Expenditure per year
Year = 12 
YearlyExpenditure = Total * Year
print("company's yearly Expenditure is ", YearlyExpenditure)

