#Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    
    try:
        #Prompt the user for a temperature to convert
        temperature = float(input("Enter the temperature to convert: "))

        #Ask whether the input is in Celsius or Fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit?(C/F): ").strip().upper()

        if unit == "C":
            print(f"{temperature}°C is {convert_to_fahrenheit(temperature):.2f}°F")
        elif unit == "F":
            print(f"{temperature}°F is {convert_to_celsius(temperature):.2f}°C")
        else:
            print("Invalid input. Please enter 'C' or 'F'.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
