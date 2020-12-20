# ASA Learning - Explained in Minutes Series
# LIKE, SHARE and SUBSCRIBE to ASA LEARNING YouTube Channel
# SinQ/CosQ in Advance!!!

# import pyfiglet 
from pyfiglet import Figlet
#FIGlet prints its input using large fancy characters made up of ordinary chars

figlet = Figlet(font="Standard")
print(figlet.renderText("ASA Learning"))

text="ASA"
listoffonts=["isometric1", "larry3d", "slant","roman",
             "alphabet","ogre","3-d","digital",
             "alligator","banner3-D","dotmatrix"]
for i in listoffonts:
    figlet = Figlet(font=i)
    print("Font :",i)
    print(figlet.renderText(text))
 
# Pyfiglet can be used to decorate the normal code to make it attractive
import pyfiglet
print(pyfiglet.FigletFont.getFonts())
# Add new font use the following command to install it
#pyfiglet -L <path of the font file>
