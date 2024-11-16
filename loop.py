def multiplication_table(n):
    for i in range(1,11):
        print(n,"x",i,"=",n*i)

n=input("Enter table number: ")
n=int(n)

print(multiplication_table(n))