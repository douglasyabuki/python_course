# Solved Exercise: calculating loan dates and installments
# John took out a loan of 1,000,000
# to pay it off in 5 years.
# The date he took the loan was
# 12/20/2020 and the due date for each installment
# is on the 20th of each month.
# - Create the loan date
# - Create the final payment date
# - Show all due dates and the value of each installment
from datetime import datetime
from dateutil.relativedelta import relativedelta

total_amount = 1_000_000
loan_date = datetime(2020, 12, 20)
delta_years = relativedelta(years=5)
end_date = loan_date + delta_years

installment_dates = []
installment_date = loan_date
while installment_date < end_date:
    installment_dates.append(installment_date)
    installment_date += relativedelta(months=+1)

num_installments = len(installment_dates)
installment_value = total_amount / num_installments

for date in installment_dates:
    print(date.strftime('%d/%m/%Y'), f'R$ {installment_value:,.2f}')

print()
print(
    f'You borrowed R$ {total_amount:,.2f} to pay '
    f'in {delta_years.years} years '
    f'({num_installments} months) with installments of '
    f'R$ {installment_value:,.2f}.'
)
