# fact = int(input("enter the nop. "))
# def fact(fact):
#     for i in range(1,fact):
#         fact = i*(i+1)
#         return fact
#     print(fact)
# fact(8)
def factorial(n):
    fac = 1
    for i in range(n):
        fac = fac * (i +1)
    return fac
num = int(input("enter the no.  "))
print(factorial(num))