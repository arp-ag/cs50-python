# rough practice 3 :-
# returning bool value : True, False
# return True if x%2==0 else False


def main():
    x=int(input("Enter x: "))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(x):
    '''if(x%2==0): return True
    else: return False'''
    
    #return True if x%2==0 else False
    
    return (x%2==0)
    
main()