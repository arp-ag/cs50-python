# practice code 1 :-

# ValueError: invalid literal for int() with base 10: 'cat'
# Its better to not generalize the error being caught,
# as it might hide some bugs and might make it difficult to figure out the issue,
# preferred being specific, like ValueError.

""" 
try:
    num=int(input("what's x? ")) # ValueError
    print(f"x is: {num}") 
except ValueError:
    print("x is not an integer") 
"""

# try to put least num of lines in try block, reduces work.
""" 
try:
    x=int(input("what's x? ")) 
    # ValueError happening in RHS, value not getting assigned to x(LHS).
except ValueError:
    print("x is not an integer")
# if nothing goes wrong...
else: 
    print(f"x is: {num}")   # NameError if outside else block.
"""
""" 
while True:
    try:
        x=int(input("What is x? "))
    except ValueError:
        print("Enter integer value.")
    else:
        print(f"x is {x}")
        break
 """

# pass keyword
# better code:

def main():
    x=get_int("Enter and int value: ")
    print(f"x is: {x}")

def get_int(msg):
    while True:
        try:
            return(int(input(msg)))
        except ValueError:
            pass

main()

# raise keyword