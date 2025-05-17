temperature= int(input("Enter the temperature in Celsius: "))

if temperature < 0:
    print("It's freezing!")
elif temperature == 0:
    print("It's freezing point.")
elif temperature >= 0 and temperature <= 20:
    print("It's cold.")
elif temperature > 20 and temperature <= 30:
    print("It's warm.")
else:
    print("It's hot!")