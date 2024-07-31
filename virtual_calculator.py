def Add(x,y):
    return x + y

def Sub(x,y):
    return x - y

def Mul(x,y):
    return x * y

def Div(x,y):
    return x / y


print("\n\nWelcome to Virtual Basic Calculator!")
print("\nThis calculator can only perform operations for two entered integer numbers and can only perform simple four operations.")

num1 = int(input("\nPlease enter the first number: "))
print("\n* Operation List *")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division\n")

opr = (input("Please enter the operation's number what did you choose: "))


while(True):
    if opr in ['1' , '2' , '3' , '4']:
        break

    else:
        print("\nPlease select one of the operations indicated between 1 and 4!")

num2 = int(input("\nPlease enter the second number: "))

if opr == '1':
    print(f"\n{num1} + {num2} = {Add(num1,num2)}\n")

elif opr == '2':
    print(f"\n{num1} - {num2} = {Sub(num1,num2)}\n")

elif opr == '3':
    print(f"\n{num1} * {num2} = {Mul(num1,num2)}\n")

elif opr == '4':
    print(f"\n{num1} / {num2} = {Div(num1,num2)}\n")

