## 2. opening a file 

file = open("Text.txt", "r")  #read

file = open("Text.txt", "w") #write

file = open("Text.txt", "a") #append

file = open("Text.txt", "rb") #read binary

file = open("Text.txt", "wb") #write binary



## 3. closing a file

#file.close()   

#Recommended method:
with open("Text.txt","r") as f:
    data = f.read()
        


