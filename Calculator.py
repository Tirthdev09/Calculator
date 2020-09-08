#This is For Adding
def Add(x, y):
    return x + y

#This is For Subtracting
def Sub(x, y):
    return x - y

#This is For Multiplication
def Multi(x, y):
    return x * y

#This is For Division
def Div(x, y):
    return x / y

print("Select Operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter Choice(1/2/3/4)")
num1 = float(input("Enter The First Number"))
num2 = float(input("Enter The Second Number"))
if choice == "1":
           print(num1, "+", num2, "=", Add(num1, num2))
if choice == "2":
           print(num1, "-", num2, "=", Sub(num1, num2))
if choice == "3":
           print(num1, "*", num2, "=", Multi(num1, num2))
if choice == "4":
           print(num1, "/", num2, "=", Div(num1, num2))

input("Press Enter To Exit")
