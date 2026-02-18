file = open("coding.txt", "r")
print(file.read())
file.close()

file_write = open("coding.txt", "w")
file_write.write("Hello, this file is in write mode.")
file_write.write("Content will be overwritten.")
file_write.close()

file_append = open("coding.txt", "a")
file_append.write("\nThe file is in append mode.")
file_append.write("Content will be added to existing file.")
file_append.close()