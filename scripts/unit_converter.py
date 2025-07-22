def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def in_to_cm(i):
    return i * 2.54

def cm_to_in(cm):
    return cm / 2.54

def lb_to_kg(lb):
    return lb * 0.453592

def kg_to_lb(kg):
    return kg / 0.453592

def main():
    print("Welcome to Unit Converter!")
    print("What would you like to convert?")
    print("Input 1 for Celsius to Fahrenheit")
    print("Input 2 for Fahrenheit to Celsius")
    print("Input 3 for inches to centimeters")
    print("Input 4 for centimeters to inches")
    print("Input 5 for pounds to kilograms")
    print("Input 6 for kilograms to pounds")

    choice = input("Enter option (1-6): ")

    if choice == '1':
        val = float(input("Enter Celsius: "))
        print(f"{val}°C is {c_to_f(val):.2f}°F")
    elif choice == '2':
        val = float(input("Enter Fahrenheit: "))
        print(f"{val}°F is {f_to_c(val):.2f}°C")
    elif choice == '3':
        val = float(input("Enter inches: "))
        print(f"{val} inches is {in_to_cm(val):.2f} centimeters")
    elif choice == '4':
        val = float(input("Enter centimeters: "))
        print(f"{val} centimeters is {cm_to_in(val):.2f} inches")
    elif choice == '5':
        val = float(input("Enter pounds: "))
        print(f"{val} pounds is {lb_to_kg(val):.2f} kilograms")
    elif choice == '6':
        val = float(input("Enter kilograms: "))
        print(f"{val} kilograms is {kg_to_lb(val):.2f} pounds")
    else:
        print("Invalid choice. Please run the program again and select a valid option.")

if __name__ == "__main__":
    main()
