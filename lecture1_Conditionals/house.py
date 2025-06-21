# rough practice 4 :-
# match...case keyword (similar to Switch...case)
# no break statement needed. no default (instead case _: )
# use single | for or 

name=input("enter name: ")
match name:
    case "Harry" | "Hermionie" | "Ron" :
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who?")