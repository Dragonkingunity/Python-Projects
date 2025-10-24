base_income = float(input('how much you make a month?\n'))
food = float(input('How much do you spend on food a month\n'))
important_bills_cost = {544.4, 240.33, 60, 40, 400, 45, 12, 100}
nonimportant_bills_cost = {16.04}
savings = float(input('How much do you want to save?\n'))
bill_number = 0

with open("budget.txt", "w") as file:
    file.write("This is your saved budget!\n")

with open("budget.txt", "a") as file:
    file.write("Base Income: " + str(base_income) + "\n")

income = base_income - food
print(f"Saved for food throughout the month {food}, income left {income} \n")

with open("budget.txt", "a") as file:
    file.write("Food: " + str(food) + "\n")

for bill in important_bills_cost:
    bill_number += 1
    income = income - bill
    print(f"This is what you have left after {bill_number}: {bill}, Remaining income: {income}", "\n")

    with open("budget.txt", "a") as file:
        file.write("Important bills: " + str(bill) + "\n")

with open("budget.txt", "a") as file:
    file.write("Income left: " + str(income) + "\n")


income = income - savings
print(f"This is what you have left after saving {savings}, Remaing income: {income} \n")

with open("budget.txt", "a") as file:
    file.write("Savings: " + str(savings) + "\n")

with open("budget.txt", "a") as file:
    file.write("Income left: " + str(income) + "\n")

for n_bill in nonimportant_bills_cost:
    bill_number += 1
    income = income - bill
    print(f"This is what you have left after {bill_number}: {n_bill}, {income}", "\n")

    with open("budget.txt", "a") as file:
        file.write("Non Imporant bills: " + str(bill) + "\n")

with open("budget.txt", "a") as file:
    file.write("Income left: " + str(income) + "\n")

print('This is how much you have left after every thing. Amount left: ', income)


with open("budget.txt", "r") as file:
    budget = file.read()
print(budget)