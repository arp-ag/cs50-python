# rough practice 2:-

# command line arguments.
# sys library/ module
# sys.argv [argument vector]

import sys
""" print("hello, my name is", sys.argv[1]) """
# python name.py Arpita 
# hello, my name is Arpita
# IndexError 

# sys.argv[0] is name of program. like in c.
""" 
if len(sys.argv)<2:
    print("too few arguments")
elif len(sys.argv)>2:
    print("too many arguments")
else:
    print("hello my name is", sys.argv[1])
 """

# sys.exit
""" 
if len(sys.argv)<2:
    sys.exit("too few arguments")
elif len(sys.argv)>2:
    sys.exit("too many arguments")
print("hello my name is", sys.argv[1])
 """

# multiple arguments at once
""" 
if len(sys.argv)<2:
    sys.exit("too few arguments")
for arg in sys.argv:
    print("hello my name is", arg)
 """

# slices [of a list] ([_:_:_])
""" 
if len(sys.argv)<2:
    sys.exit("too few arguments")
print("hello my name is:", end=" ")
# if i use [1:-1] it will skip the last argument
for arg in sys.argv[1:]: 
    print(arg, end=" ")
 """