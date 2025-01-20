#calculate and provide feedback on a user’s monthly savings and potential future savings using these variables
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

#Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

#Print the result
print(f"Your monthly savings are {monthly_savings}")

#Calculate the project annual savings
#Rate = 0.05 Simple annual interest rate
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#Print the results
print(f"Projected savings after one year, with interest, is: {projected_savings}")