def main():
    text=input("Input: ")
    print("Output:", remove_vovels(text))
def remove_vovels(txt):
    vovels="aeiouAEIOU"
    res=""
    for ch in txt:
        if ch not in  vovels:
            res+=ch
    return res

main()