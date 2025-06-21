# a function defination should be done before it is called.
# or a main function may be created for the body, that might be called at the end of the program.
# print(f"{Python expressions}")  in Python utilizes an f-string (formatted string literal)
# ALSO! a number to be displayed, put in this format practices number formatting. Eg: 100,000,000.00

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return round(float(d),1)


def percent_to_float(p):
    return round(float(p)/100,2)


main()