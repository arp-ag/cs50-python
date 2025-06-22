from random import randint
while True:
    try:
        level=int(input("Level: "))
        if level>0:
            break
    except ValueError:
        pass
res=randint(1,level)
while True:
    try:
        guess=int(input("Guess: "))
        if guess<1:
            continue
    except ValueError:
        pass
    if guess<res:
        print("Too small!")
    elif guess > res:
        print("Too large!")
    else:
        print("Just right!")
        break