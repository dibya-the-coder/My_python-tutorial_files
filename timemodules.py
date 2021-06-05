import time

# initial = time.time()
# print(initial)
# k = 0
# while(k<55):
#     print("lolme")
#     k += 1
# print(time.time() - initial)
# initial2 = time.time()
# for i in range(4):
#     print("lol")
# print(time.time()-initial2)

localtime = time.asctime(time.localtime(time.time()))
print(localtime)