##Writing

# with open("file.txt", "w") as f:
#     f.write("Hello World! \nThis is working with text files as writng")
#     f.write("\nWelcome to python")


##Reading

# with open("File.txt", "r")as f:
#     print(f.read())  #o/p in terminal


##reading line by line

with open("file.txt","r") as f:
    for line in f:
        print(line.strip())
