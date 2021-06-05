# w for write mode

# r for read mode

# a for append mode (add lines to the content)

# f = open("lol me.txt", "w")
# a = f.write("whats up i am fine  ok bro\n ")
# print(a)
# f.close()

# r+ for read and write both


f = open("lol me.txt", "r+")
f.write("whats up i am fine  ok bro\n ")
f.write("thank you")
f.write("kug yaar")
print(f.read())
# print(a)
f.close()