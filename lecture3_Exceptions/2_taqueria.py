# used title() to title cased
# print(f"${Total:.2f}") 

def main():
    Total=0.0
    menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    while True:
        try:
            item=input("Item: ").title()
        except EOFError:
            break
        if item in menu:
            Total+=menu[item]
            print(f"Total: ${Total:.2f}")
        
        

main()