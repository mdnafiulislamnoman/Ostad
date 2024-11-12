#Project Declaration
print("My calculator project for Ostad")

print("Please choose your desired option to execute the operation")
#Options
print("Option 1: Addition")
print("Option 2: Subtraction")
print("Option 3: Multiplication")
print("Option 4: Division")

print("Enter 1,2,3,4 to choose the preferable option:")

#Taking input
option = int(input())

#Matching condition
if option == 1:
    print("Enter your 1st number:")
    na1 = int(input())
    print("Enter your 2nd number:")
    na2 = int(input())
    print(na1+na2)

elif option == 2:
    print("Enter your 1st number:")
    ns1 = int(input())
    print("Enter your 2nd number:")
    ns2 = int(input())
    print(ns1-ns2)

elif option == 3:
    print("Enter your 1st number:")
    nm1 = int(input())
    print("Enter your 2nd number:")
    nm2 = int(input())
    print(nm1*nm2)

elif option == 4:
    print("Enter your 1st number:")
    nd1 = int(input())
    print("Enter your 2nd number:")
    nd2 = int(input())
    print(nd1/nd2)

else:
    print("Invalid operation")

