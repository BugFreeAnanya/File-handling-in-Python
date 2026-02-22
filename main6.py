with open("codingal.txt", "w") as file:
    file.write("This is a new file created using 'with' statement.")
file.close()

with open("codingal.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
file.close()