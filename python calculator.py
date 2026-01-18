import math

def show_menu():
    print("\n🧮 Scientific Calculator")
    print("-" * 30)
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Sin(x)")
    print("8. Cos(x)")
    print("9. Tan(x)")
    print("10. Log(x)")
    print("11. Log10(x)")
    print("12. Factorial(x)")
    print("0. Exit")
    print("-" * 30)

while True:
    show_menu()
    choice = input("Choose an option: ")

    try:
        if choice == "0":
            print("👋 Goodbye!")
            break

        elif choice in ["1", "2", "3", "4", "5"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", a + b)
            elif choice == "2":
                print("Result:", a - b)
            elif choice == "3":
                print("Result:", a * b)
            elif choice == "4":
                print("Result:", a / b)
            elif choice == "5":
                print("Result:", math.pow(a, b))

        elif choice == "6":
            x = float(input("Enter number: "))
            print("Result:", math.sqrt(x))

        elif choice == "7":
            x = float(input("Enter angle in radians: "))
            print("Result:", math.sin(x))

        elif choice == "8":
            x = float(input("Enter angle in radians: "))
            print("Result:", math.cos(x))

        elif choice == "9":
            x = float(input("Enter angle in radians: "))
            print("Result:", math.tan(x))

        elif choice == "10":
            x = float(input("Enter number: "))
            print("Result:", math.log(x))

        elif choice == "11":
            x = float(input("Enter number: "))
            print("Result:", math.log10(x))

        elif choice == "12":
            x = int(input("Enter integer: "))
            print("Result:", math.factorial(x))

        else:
            print("❌ Invalid choice")

    except Exception as e:
        print("⚠️ Error:", e)
