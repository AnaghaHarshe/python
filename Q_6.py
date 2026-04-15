with open ("count_lines_Word_char.txt","w")as file:
    file.write("Hello Python\n")
    file.write("File Handling is easy")

with open ("count_lines_Word_char.txt","r")as file:
    content = file.read()
    
lines = content.split("\n")
num_lines = len(lines)

words = content.split()
num_words = len(words)

num_characters = len(content)

print("Number of lines:",num_lines)
print("Number of words:", num_words)
print("Number of characters:", num_characters)