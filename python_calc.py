def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
       return "Error: Division by zero is not allowed."
    return a/b
def even_or_odd(n):
    if n!=int(n):
      return "Error: Even/Odd check needs a whole number."
    return "Even" if int(n)%2==0 else "Odd"
def percentage(a,b):
        if b==0:
            return"Enter: Cannot calculate percentage of zero"
        return(a/b)*100
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
def show_menu():
    print("\n==== PYTHON CALCULATOR ====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even/Odd")
    print("6. Claculate Percentage")
    print("7. Exit")

def main():
    while True:
        show_menu()
        choice= input("Enter your choice (1-7): ").strip()
        if choice=="7":
            print("Goodbye!")
            break
        if choice in ("1","2","3","4"):
            a=get_number("Enter first number: ")
            b=get_number("Enter second number: ")
            if choice=="1":
                print (f"Result: {a}+{b}={add(a,b)}")
            elif choice=="2":
                print (f"Result: {a}-{b}={subtract(a,b)}")
            elif choice=="3":
                print (f"Result: {a}×{b}={multiply(a,b)}")
            elif choice=="4":
                print (f"Result: {a}/{b}={divide(a,b)}")
        elif choice=="5":
            n=get_number("Enter a number: ")
            print(f"Result: {n} is {even_or_odd(n)}")
        elif choice=="6":
            a=get_number("Enter the first number(part):")
            b=get_number("Enter the second number (whole):")
            if b==0:
                print("Error: Cannot calculate percentage of zero.")
            else:
              result=percentage(a,b)
              print(f"Result: {a} is {result}% of {b}")
        else:
            print("Invalid choice. Please select 1-7")
if __name__=="__main__":
 main()
        
