#create a new file
new_file = open("New_File.txt", "x")
new_file.close()

#check if a file exists
import os
print("Checking if my_file exists or not....")
if os.path.exists("New_File.txt"):
    os.remove("New_File.txt")
else:
    print("The file does not exist")

#create a new if it doesn´t
my_file = open("my_file.txt", "w")
my_file.write("Hi! I am Penguin and I am 1 yr old.")
my_file.close()


import os
#delete file named codingal
os.remove("codingal.txt")

#delete the folder
os.rmdir("C:\\Users\\imran\\OneDrive\\Documents\\Python course\\Lesson 15\\Folder")