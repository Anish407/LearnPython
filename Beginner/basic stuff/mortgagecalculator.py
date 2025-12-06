money_owed= float(input("Enter the amount of money you owe: "))
annual_interest_rate= float(input("Enter the annual interest rate (as a percentage): "))
months= int(input("Enter the number of months to pay off the mortgage: "))
monthly_payment= float(input("Enter the monthly payment amount: "))


monthly_interest_rate= annual_interest_rate / 100 / 12

for month in range(1, months + 1):
    interest= money_owed * monthly_interest_rate
    principal= monthly_payment - interest
    money_owed -= principal
    if money_owed < 0:
        money_owed = 0
    print(f"Month {month}: Payment: ${monthly_payment:.2f}, Interest: ${interest:.2f}, Principal: ${principal:.2f}, Remaining Balance: ${money_owed:.2f}")
    if money_owed == 0:
        print("Mortgage paid off!")
        break