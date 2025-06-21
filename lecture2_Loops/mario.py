# rough practice 3:-
# nested loops

def main():
    a, b=input("enter no of rows and columns: ").split()
    shape(int(a),int(b))
def shape(x,y):
    for i in range(x):
        for i in range(y):
            print("O", end=(""))
        print()


main()