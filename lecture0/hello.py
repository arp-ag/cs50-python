#ask user's name
name=input("What is your name? ").strip().title()
# name=name.strip() #trims extra spaces in start and end
# name=name.capitalize() #only first alphabet
# name=name.title() #every first word
first, last=name.split(" ") #need to enter name with 2 words only!!
#Say hello to user
# print("hello Mr/Ms.",name)
# print("hello Mr/Ms. "+name)
print(f"Hello {first}")