# open two files at once

with open("files1.txt","w")as f1, open("file2.txt","w")as f2:
    f1.write("This is file 1 \n")
    f2.write("This is file 2 \n")
    
print("Both files written successfully.")