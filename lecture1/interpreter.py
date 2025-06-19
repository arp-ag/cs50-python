# used eval(expr)
# displayed floating-point value formatted to one decimal place

expr=input("Expression: ")
print(round(float(eval(expr)),1))