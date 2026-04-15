# with open("data.txt","w")as file:
#     file.write(" ")           this is for try


try:
    with open("data.txt","r")as file:
        print(file.read())
        
        
except FileNotFoundError:
    print("Error: File not found Please check the file name.")

