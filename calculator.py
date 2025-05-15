def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

print("Welcome to My Simple Calculator!")
print("Pick an operation to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    option = input("Choose (1/2/3/4): ")

    if option not in ['1', '2', '3', '4']:
        print("Invalid choice. Please select a valid option.")
        continue

    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
    except ValueError:
        print("Oops! Please enter numbers only.")
        continue

    if option == '1':
        output = add(n1, n2)
        print(f"Result: {n1} + {n2} = {output}")
    elif option == '2':
        output = subtract(n1, n2)
        print(f"Result: {n1} - {n2} = {output}")
    elif option == '3':
        output = multiply(n1, n2)
        print(f"Result: {n1} * {n2} = {output}")
    elif option == '4':
        output = divide(n1, n2)
        print(f"Result: {n1} / {n2} = {output}")

    repeat = input("Do you want to do another calculation? (yes/no): ").lower()
    if repeat != 'yes':
        print("Thanks for using the calculator. Goodbye!")
        break
