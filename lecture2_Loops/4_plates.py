# .isalpha()

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[0].isalpha() and s[1].isalpha:
        return False
    if not 2 <= len(s) <= 6:
        return False
    num_started=False
    for i in range(len(s)):
        if s[i].isdigit():
            if num_started==True:
                if s[i]==0:
                    return False
            else:
                num_started=True
        else:
            if num_started==True: 
                return False
    return True

main()