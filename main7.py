new_file = open("Newfile.txt", "x")
new_file.close()

import os
if os.path.exists("Myfile.txt"):
    os.remove("Myfile.txt")
else:
    print("The file does not exist.")
my_file = open("Myfile.txt", "w")
my_file.write("This is a new file created using os module.")
my_file.close()
os.remove("codingal.txt")
os.rmdir("Folder")