#  .split used
def main():
    time=input("What time is it? ")
    hrs=convert(time)
    if 7.0 <= hrs <= 8.0:
        print("breakfast time")
    elif 12.0 <= hrs <= 13.0: 
        print("lunch time")
    elif 18.0 <= hrs <= 19.0:
        print("dinner time")

def convert(t):
    hrs, mins= t.split(":")
    return round(int(hrs)+int(mins)/60,1)

main()