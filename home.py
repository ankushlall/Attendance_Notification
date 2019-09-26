from PIL import Image

img=Image.new('RGBA',(900,900))
for i in range(900):
    for j in range(900):
        img.putpixel((i,j),(i/4,0,j/4))


img.show()
