

""" 
def main():
    names=[]
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            break
    print("Adieu, adieu, to", end=" ")
    if len(names)>2:
        for nm in names[:-1]:
            print(nm, end=", ")
        print(f"and {names[-1]}")
    else:
        print(f"{names[-1]}")
main() """

import inflect
p=inflect.engine()
names=[]
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        break
print(f"Adieu, adieu, to {p.join(names)}")