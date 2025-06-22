import random


def main():
    lev=get_level()
    score=0
    for i in range(10):
        x=generate_integer(lev)
        y=generate_integer(lev)
        correct=x+y
        tries=0
        while tries<3:
            try:
                ans=int(input(f"{x} + {y} = "))
                if ans == correct:
                    score+=1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            tries+=1
        else:
            print(f"{x} + {y} = {correct}")
    print(f"score = {score}")
        


def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level==1:
        return random.randint(0, 9)
    elif level==2:
        return random.randint(10, 99)
    elif level==3:
        return random.randint(100,999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()