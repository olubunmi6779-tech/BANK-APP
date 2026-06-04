income = float(input("Enter your income: "))
expense = float(input("Enter your expense: "))

balance = income - expense

print("\n----- Bank Summary -----")
print("Income:", income)
print("Expense:", expense)
print("Balance:", balance)

#response

if balance > 0:
    print("Great! You saved some money .")
elif balance == 0:
    print("You broke even.")
else:
    print("Your expenses are more than your income , you didn't save.")