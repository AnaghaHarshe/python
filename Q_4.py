# with open("read_write.txt", "w") as file:
#     file.write("Hello World\n")

#open file in read + write mode
with open ("read_write.txt", "r+")as file:
    
    content = file.read()     #Read existing content
    print("Orignal Content:")
    print(content)
    
    file.seek(0)
    
    # Modify content (example: add new line at top)
    new_content = "Update file Content\n" + content
    
    file.write(new_content)
    
    ## Update file Content is print how many time run that time it will print 