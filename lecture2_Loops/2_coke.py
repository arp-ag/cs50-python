def main():
    due=0
    while due<50:
        print(f"Amount Due: {50-due}")
        due+=int(input("Insert coin: "))
    print(f"Change Owed: {due-50}")

main()