import os

print("Testing  input parameter. Printing message and writing it to hello-world.txt")
hello_message = os.getenv('hello_message')
print(hello_message)

# Create a file 
f = open("hello-world.txt", "w")
f.write(hello_message)
f.close()