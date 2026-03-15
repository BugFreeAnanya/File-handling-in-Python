with open("MY_file.txt", "w") as file:
    file.write("Hi! I am learning file handling in python.")
file.close()

with open("MY_file.txt", "r") as file:
    data = file.readlines()
    print("The words in the file are: ")
    for line in data:
        word = line.split()
        print(word)
file.close()    