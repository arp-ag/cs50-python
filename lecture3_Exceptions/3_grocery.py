grocery={}
while True:
    try:
        item  = input()
    except EOFError: # ctrl+Z+enter
        break
    
    if item in grocery:
        grocery[item]+=1
    else:
        grocery[item]=1
for i in sorted(grocery):
    print(f"{grocery[i]} {i.upper()}")