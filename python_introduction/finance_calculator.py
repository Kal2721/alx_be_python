monthly_income = input("Enter your monthly income: ") # income per month
monthly_expenses = input("Enter your total monthly expenses: ") # expenses per month

monthly_savings = float(monthly_income) - float(monthly_expenses)
yearly_savings = monthly_savings * 12
rate = 0.05

projected_savings = float(yearly_savings + (yearly_savings * rate))

print("Your monthly savings are $", monthly_savings)
print("Projected savings after one year, with interest, is: $", projected_savings)