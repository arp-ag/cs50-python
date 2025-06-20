# camel case to snake case
# used .isupper(), .lower()

def main():
    str=input("camelCase: ")
    print("snake case:",camel_to_snake(str))

def camel_to_snake(str):
    res=""
    for ch in str:
        if ch.isupper():
            res+="_"+ch.lower()
        else:
            res+=ch
    return res

main()