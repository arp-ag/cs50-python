def main():
    item=input("Item: ")
    calories(item)
def calories(item):
    d={"Apple":"130", "Avocado":"50", "Banana":"110", "Cantaloupe":"50", "Grapefruit":"60",}
    for i in d:
        if i.lower() == item.lower():
            print("Calories:",d[i])

main()