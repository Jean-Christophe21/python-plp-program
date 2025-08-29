#encoding utf-8

def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, try again.")

val1 = read_float("Enter the first value: ")
val2 = read_float("Enter the second value: ")

print(
    "Enter:\n"
    "       1 for Addition\n"
    "       2 for Subtraction\n"
    "       3 for Multiplication\n"
    "       4 for Division"
)

choice = input("Your choice (1-4): ").strip()

result = None
op = ""

if choice == "1":
    result = val1 + val2
    op = "+"
elif choice == "2":
    result = val1 - val2
    op = "-"
elif choice == "3":
    result = val1 * val2
    op = "*"
elif choice == "4":
    op = "/"
    if val2 == 0:
        print("Error: Division by zero.")
    else:
        result = val1 / val2
else:
    print("Invalid choice.")

if result is not None:
    print(f"{val1} {op} {val2} = {result}")
