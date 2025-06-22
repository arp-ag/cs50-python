# You can install pyfiglet with:
# pip install pyfiglet

# from pyfiglet import Figlet
# figlet = Figlet()
# You can then get a list of available fonts with code like this:
# figlet.getFonts()
# You can set the font with code like this, wherein f is the font’s name as a str:
# figlet.setFont(font=f)
# And you can output text in that font with code like this, wherein s is that text as a str:
# print(figlet.renderText(s))



import sys
import random
from pyfiglet import Figlet

if len(sys.argv)!=1 and len(sys.argv)!=3:
    sys.exit()
figlet= Figlet()
if len(sys.argv)==3:
    if(sys.argv[1] not in ["-f", "--font"]):
        sys.exit("Invalid flag.")
    f=sys.argv[2]
    if f not in figlet.getFonts():
        sys.exit("Invalid font.")
    figlet.setFont(font=f)
else:
    fonts=figlet.getFonts()
    figlet.setFont(font=random.choice(fonts))
s=input("Input: ")
print(figlet.renderText(s))
