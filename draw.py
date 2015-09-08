import index as Image

img = Image.loadImage("./img/mao.jpg")
img = Image.resizeImage(img,100,100)

data = img.getdata()
colors = []

print(list(data))

for i in range(0, img.size[0]):
    for j in range(0, img.size[1]):
        color = data[i * 4 + j]

        average = (color[0] + color[1] + color[2]) / 3
        colors.append(int(average))

print(colors)
