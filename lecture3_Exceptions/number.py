# practice code :-
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

try:
    num=int(input("what's x? ")) 
    # ValueError happening in RHS, value not getting assigned to x(LHS).
except ValueError:
    print("x is not an integer")
# if nothing goes wrong...
else: 
    print(f"x is: {num}")   # NameError if outside else block.