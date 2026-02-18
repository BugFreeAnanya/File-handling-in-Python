file = open("codingal.txt", "r")
print("Reading first line of the file")
print(file.readline())
file.close()

file = open("codingal.txt", "r")
print("Reading multiple lines of the file")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open("codingal.txt","r")
print("Looping through lines of the file")
for line in file:
    print(line)
file.close()