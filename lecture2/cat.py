# rough practice 1:-

# LOOPS
# WHILE
"""
i=0 
while i<3:
    print("meow")
    i+=1
 """
# FOR, LIST
# Function: RANGE - integer values only (0 to n-1)
# for i in list[0,1,2]:
# for i in range(40): 
""" 
for _ in range (4): # we dont care about the variable named i, no use for us 
    print("meow")
 """

# print("meow" * 3) prints in same line without gaps  
# print("meow\n" * 3, end="") # end="" overrides the last default \n that comes with the print syntax.

""" 
n=int(input("how many times meow: "))
print("meow\n" * n, end="")
 """

# break

def main():
    num=get_num()
    meow(num)

def get_num():
    while True:
        num=int(input("how many times meow: "))
        if num>0:
            return num

def meow(num):
    print("meow\n" * num, end=(""))

main()