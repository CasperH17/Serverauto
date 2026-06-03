def check_temperature(temperature):
    """This function checks the temperature and prints a message."""
    if temperature < 10:
        print("It is cold outside")
    elif temperature <= 20:
        print("The weather is okay")
    else:
        print("It is warm outside")


print("Welcome to the weather program")

temperatures = [5, 15, 25]

for temperature in temperatures:
    print("The temperature is " + str(temperature) + " degrees")
    check_temperature(temperature)

print("Program finished")