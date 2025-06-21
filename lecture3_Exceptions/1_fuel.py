# used map()
# used self declared exception
# displayed error msg without all those red lines.

class InvalidInputError(Exception):
    pass
def main():
    fuel=input("Fraction: ")
    fuel_gauge(fuel)
def fuel_gauge(fuel):
    x,y=map(int, fuel.split("/"))
    try:
        if(x>y):
            raise InvalidInputError("x is greater than y")
        p=round(x/y*100)
    except (ValueError, ZeroDivisionError, InvalidInputError) as e:
        print(e)
        pass
    else:
        if(p<=1):
            print("E")
        elif(p>=99):
            print("F")
        else:
            print(f"{p}%")
main()