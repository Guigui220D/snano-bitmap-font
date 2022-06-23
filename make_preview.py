from PIL import Image, ImageColor

font = Image.open("font.png");

width = font.size[0]
height = font.size[1]

for x in range(width):
    for y in range(height):
        if font.getpixel((x, y)) == 0:
            font.putpixel((x, y), (255, 255, 255))
        else:
            font.putpixel((x, y), (0, 0, 1))
            
font = font.resize([width * 4, (height - 20) * 4], resample = Image.NEAREST, box = (0, 20, 128, 80))
font.show()

font.save("preview.png")