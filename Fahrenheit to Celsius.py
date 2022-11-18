from time import sleep

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

def main():
    print("This program converts temperatures from Fahrenheit to Celsius.")
    print()

    fahrenheit = eval(input("Enter the temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print("The temperature in Celsius is", celsius)
    sleep(15)
main()