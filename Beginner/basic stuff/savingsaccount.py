
amount_to_be_saved = float(input("Enter the amount you want to save: "))
interest = float(input("Enter the annual interest rate (as a percentage): "))
monthly_saving = float(input("Enter the amount you can save each month: "))

months = int(input("Enter the number of months you plan to save: "))
total_saved = 0

monthly_interest_rate = interest / 100 / 12

for month in range(1, months + 1):
    total_saved += monthly_saving
    interest_earned = total_saved * monthly_interest_rate
    total_saved += interest_earned

    print(f"Month {month}: Total Saved: ${total_saved:.2f}, Interest Earned: ${interest_earned:.2f}")

    if total_saved >= amount_to_be_saved:
        print(f"Congratulations! You've reached your goal of ${amount_to_be_saved:.2f} in {month} months.")
        break

