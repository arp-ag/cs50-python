# used .lower() for case-insensitivity

answer=input("The Answer to the Great Question is? ").lower()
match answer:
    case "forty-two" | "forty two" | "42":
        print("Yes")
    case _:
        print("No")