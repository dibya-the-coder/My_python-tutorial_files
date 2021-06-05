# for i in range(4):
#
#     for j in range(4):
#         print("*",end="")
#     print()
# for i in range(6):
#     for j in range(i+1):
#         print("*",end="")
#     print()
# for i in range(6):
#     for j in range(i+1):
#         print(j,end="")
#     print()
# i = int(input("entar the no of row: "))
# for i in range(i):
#     for j in range(i +1):
#         print(i*j, end="")
#     print()
n = int(input("enter the no of rows: "))
for i in range(n):
    for j in range(n-i):
        print("$",end="")
    print()
