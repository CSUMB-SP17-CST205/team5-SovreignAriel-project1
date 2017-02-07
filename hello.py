from PIL import Image

def medianOdd(myList): #from documents on CST 205
# Store list length in the variable listLength
    listLength = len(myList)
# Sort the list
    sortedValues = sorted(myList)
# Location of middle value. Subtract one because of zero index
    middleIndex = ((listLength + 1)/2) - 1
# Return the object located at that index
    return sortedValues[middleIndex]
    
imgs = []    
for p in range (1, 10):
    imgs.append(Image.open(str(p) + ".png"))
w, h = imgs[0].size
editedImage = Image.new("RGB", (w, h), 0)

pixels = editedImage.load()

for x in range(w):
    for y in range(h):
        red = []
        green = []
        blue = []
        for i in (imgs):
            newRed, newGreen, newBlue = i.getpixel((x, y))
            red.append(newRed)
            green.append(newGreen)
            blue.append(newBlue)
            
        pixels [x, y] = (medianOdd(red), medianOdd(green), medianOdd(blue))

editedImage.save("project1Team5Ariel.png")