""" 
names=[]
for _ in range(3):
    names.append(input("What's your name? "))
for name in sorted(names):
    print(f"hello {name}")
 """

""" 
name=input("What's your name? ")
file=open("names.txt", "w") 
# "w" overwrites each time
file.write(name)
file.close()
 """
# PROBLEM: creates new if doesnt exist

""" 
name= input("What's your name? ")
file=open("names.txt", "a") # append
file.write(name)
file.close()
 """
# PROBLEM: puts input without any space, just appending it.

""" 
name= input("What's your name? ")
file=open("names.txt", "a") # append
file.write(f"{name}\n")
file.close()
 """

# with keyword : automatically open and close file