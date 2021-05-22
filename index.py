print("hi")
file = open("data.txt", mode="r")
try:
    line = file.readline()
    print(line)
except:
    pass