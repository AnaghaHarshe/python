with open ("example.txt","w")as file:
    file.write("Hello file is crated !")


#Read Mode ("r") -> read files content  
with open("example.txt","r")as file:
    content = file.read()
    print("Read mode output:")
    print(content)
    

# Append mode ("a") -> adds data at end of files 
with open ("example.txt","a")as file:
    file.write("\nThis line is added using append mode.\n")
print("\nAppend mode executed")

#Read agein to show updated content
with open("example.txt","r")as file:
    content = file.read()
    print("Final file content")
    print(content)
    