# # 7. Write a program to search a given string in a text file.

# search_word = input("Enter word to search: ")

# with open("W_search.txt","w")as file:
#     file.write("Hello python \n This is file handling ")

# with open("W_search.txt","r")as file:
#     content = file.read()
    
# if search_word in content:
#     print(f"{search_word} Word found in file.")
# else:
#     print(f"{search_word} Word not found.")
    
# #-------------------------------------------------------------------------------------------------------------


# # 8. Write a program to replace a word in a text file with another word.

# old = input("Enter old word: ")
# new = input("Enter new word: ")

# with open("W_replace.txt","r")as file:
#     contnt = file.read()
    
# updated_content = contnt.replace(old, new)

# with open("W_replace.txt","w")as file:
#     file.write(updated_content)
    
# print("Word replace successfully.")


# #---------------------------------------------------------------------------------------------------------------

# #9. Write a program to read a file line by line and display only lines containing a specific keyword

# keyword = input("Enter keyword to search:")  # case sensitive capital / small letters

# with open("KeyW_search.txt","r")as file:
#     for line in file:
#         if keyword in line:
#             print(line, end = "")


# #---------------------------------------------------------------------------------------------------------------

# # 10 Write a program to copy the contents of one text file into another.

# try:
#     with open("source.txt","r") as source, open("destination.txt", "w")as dest:
#         dest.write(source.read())
#     print("File copied Successfully.")
    
# except FileNotFoundError:
#     print("Source file not foud.")
    
    
# #---------------------------------------------------------------------------------------------------------------

# #11. Write a program to check whether a file exists using the os module.

# import os

# filename = "D:/Languages/python/WEBI/Data Storage in files/---------"  #fill this blanks 

# if os.path.exists(filename):
#     print("File exists.")
# else:
#     print("File does not exist.")


# #---------------------------------------------------------------------------------------------------------------

# # 12. Write a program that creates a file only if it does not already exist.
# #13. Write a program to display a message if the file exists, otherwise create it.

# import os
# filename = input("Enter file name:")

# if not os.path.exists(filename):
#     with open(filename, 'w')as file:
#         print("File created successfully.")
# else:
#     print("File already exists.")
    
# #---------------------------------------------------------------------------------------------------------------

# # 14. Write a program to read and display records from a binary file.

# import pickle

# filename = "binary.dat"

# try:
#     with open(filename, 'rb')as file:
#         print("Records in the file:\n")
        
#         while True:
#             try:
#                 record = pickle.load(file)
#                 print(record)
#             except EOFError:
#                 break

# except FileNotFoundError:
#     print("File does not exist.")


# #---------------------------------------------------------------------------------------------------------------

# #15. Write a program to append new records to an existing binary file.

# import pickle

# filename = "binary.dat"

# with open(filename,'ab')as file:
#     n = int(input("How many records do you want to add? :-"))
    
#     for i in range(n):
#         print(f"\nEnter details for record{i+1}:")
#         rno = int(input("Enter ID: "))
#         name = input("Enter Name: ")
        
#         record = {"id": rno, "name": name}
#         pickle.dump(record,file)
        
# print("\nRecords appended successfully.")

# #---------------------------------------------------------------------------------------------------------------

# # 16. Write a program to display all files and folders in the current directory.

# import os

# current_dir = os.getcwd()

# print("Currnt Directory:", current_dir)
# print("\n Files and Folders:\n")

# for item in os.listdir(current_dir):
#     print(item)


