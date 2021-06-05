# # def function1():
# #     print("suscribe now")
# #
# # func2 = function1
# # del function1
# # func2()
# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return int
# # a=funcret(0)
# print(a)
# def executer(func):
#     func("this")
# executer(print)
def dec1(func1):
    def nowexec():
        print("executing values")
        func1()
        print("executed")
    return nowexec

def whoishe():
    print("lkh;sx")
whoishe = dec1(whoishe)
whoishe()