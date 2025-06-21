# used .title()
# print(f"{date[2]:04}-{date[0]:02}-{date[1]:02}")

class InvalidInput(Exception):
    pass
def main():
    months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    res=""
    while True:
        try:
            date=input("Date: ")
            if "/" in date:
                # Format: MM/DD/YYYY
                date=date.split("/")
                date[0], date[1], date[2] = int(date[0]), int(date[1]), int(date[2])
            else:
                # Format: Month DD, YYYY
                date=date.replace(",","").split()
                date[0]=months.index(date[0].title())+1
                date[1], date[2] = int(date[1]), int(date[2])
            if 0<date[2]<999 or not 0<date[1]<=31 or not 0<date[0]<=12:
                raise InvalidInput
            
        except (InvalidInput, ValueError, IndexError) as e:
            print(e)
            continue
        print(f"{date[2]:04}-{date[0]:02}-{date[1]:02}")
        break



main()