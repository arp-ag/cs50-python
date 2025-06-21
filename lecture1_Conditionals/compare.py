# rough practice 1 :-

# conditionals
'''x=int(input("Enter x: "))
y=int(input("Enter y: "))
if x>y:
    print(f"{x} (x) is greater")
elif y>x:
    print(f"{y} (y) is greater")
else:
    print("x and y are equal")'''

# or keyword
x=int(input("Enter x: "))
y=int(input("Enter y: "))
if x>y or y>x:
    print("x and y are not equal")
else:
    print("x is equal to y")