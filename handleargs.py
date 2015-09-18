import sys
import index as Image

if(len(sys.argv) < 3):
    print("lacking argvs of screen width and scrren height!")
    exit()

SW = int(sys.argv[1])/2
SH = int(sys.argv[2])-1

img = Image.loadImage("./img/mao.jpg")
img = Image.resizeImage(img,SW,SH)

data = img.getdata()
dataList = list(data)
length = len(dataList)
colors = []

for i in range(0,length):
    color = dataList[i]
    
    average = (color[0] + color[1] + color[2]) / 3
    colors.append(int(average))

for i in range(0,len(colors)):
    sys.stdout.write("00")
    if((i+1) % img.size[0] == 0):
        sys.stdout.write("\n")
