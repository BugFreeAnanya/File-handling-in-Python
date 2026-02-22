file = open("The file.txt", "r")
print(file.read(12))
file.close()

file = open("The file.txt", "r")
print(file.readline())
file.close()

file = open("The file.txt", "r")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readlines())
file.close()