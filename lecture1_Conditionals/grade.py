# rough practice 2 :
# other ways:-
# if( score<=90 and score<100 )
# if( 90<=score and score<100 )
# if( 90<=score<100 )


score=int(input("enter score: "))
if ( score >= 90 ):
    print("O")
elif( score >= 80):
    print("E")
elif( score >= 70):
    print("A")
elif( score >= 60):
    print("A")
elif( score >= 50):
    print("B")
else:
    print("Eligible to give improvement exam.")