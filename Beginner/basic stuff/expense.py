expenses= [ 10, 12.5,55, 66.7, 54.3,55.5]

totalExpenses= 0

# using for loop
for expense in expenses:
        totalExpenses += expense

print(f"Your total expenses are {totalExpenses}")
print("Your total expenses are $", totalExpenses,sep= "") # this will remove the space between $ and sum


total= sum(expenses) # using built in function

print(f"Your total expenses are $$ {total}")