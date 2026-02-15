file = open("codingal.txt")
print(file.read())
file.close()

file_write = open("codingal.txt", "w")
file_write.write("This file is in write mode.")
file_write.write("This will overwrite the previous content.")
file_write.close()

file_append = open("codingal.txt", "a")
file_append.write("\n This file is in append mode.")
file_append.write("This will add content to existing file.")
file_append.close()