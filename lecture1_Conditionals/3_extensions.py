#can't extract what condition was checked by endswith, OR use a tuple with loop
# name=input("name of a file: ")
# if name.endswith(".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip"):
#     print()

name=input("File name: ")
if(name.endswith(".gif")):
    print("img/gif")
elif(name.endswith(".jpg")):
    print("img/jpg")
elif(name.endswith(".jpeg")):
    print("img/jpeg")
elif(name.endswith(".png")):
    print("img/png")
elif(name.endswith(".pdf")):
    print("img/pdf")
elif(name.endswith(".txt")):
    print("img/txt")
elif(name.endswith(".zip")):
    print("img/zip")
else:
    print("application/octet-stream")