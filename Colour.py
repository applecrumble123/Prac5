# AliceBlue: #f0f8ff
# AntiqueWhite: #faebd7
# Aquamarine1: #7fffd4
# Azure1: #f0ffff
# beige: #f5f5dc
# bisque1: #ffe4c4
# black: #000000
# brown: #a52a2a
# BlueViolet: #8a2be2
# coral : #ff7f50

COLOURS = {'aliceblue': '#f0f8ff', 'antiquewhite': '#faebd7', 'aquamarine1': '#7fffd4', 'azure1': '#f0ffff',
           'beige': '#f5f5dc',
           'bisque1': '#ffe4c4',
           'black': '#000000', 'brown': '#a52a2a', 'blueviolet': '#8a2be2', 'coral': '#ff7f50'}

for key in COLOURS:
    print(key)
#get_colour ="blank"
while True:
    get_colour = str(input("Enter Colour: ")).lower()
    print(COLOURS.get(get_colour))

    if get_colour =="":
        break