import sys
import platform

SYSTEMTYPE = platform.system()

if SYSTEMTYPE != "Linux" and SYSTEMTYPE != "Darwin":
    print("This tool only work in Unix, sorry!")
    exit()

from PIL import Image

def resizeImage(im, width, height):
    originalW, originalH = im.size
    originalRatio = originalW / float(originalH)
    ratio = width / float(height)

    newW, newH = int(width), int(height)

    if ratio < originalRatio:
        newH = int(width / originalRatio)
    else:
        newW = int(height * originalRatio)

    if newW * 2 <= width:
        newW *= 2

    return im.resize((newW, newH), Image.ANTIALIAS)


def loadImage(path):
    try:
        return Image.open(path)
    except IOError:
        print("ERROR:The path is not a useful image path !")
        exit()


def processImage(img):
    colors = []

    data = img.getdata()
    dataList = list(data)
    length = len(dataList)

    for i in range(0, length):
        color = dataList[i]

        average = (color[0] + color[1] + color[2]) / 3
        colors.append(int(average))

    return colors


def outputColors(colors, width):
    chars = ['M', '@', '&', '%', 'm', 'H', 'w', '#', '$', 'k', '}', ']', 'd', 't', '?', '/', 'j', '*', ';', ':', 'x', '>', '-', '|', '\"', '\'', '.', ' ']

    for i in range(0, len(colors)):
        sys.stdout.write(chars[colors[i] / 10])
        if (i + 1) % width == 0:
            sys.stdout.write("\n")


if __name__ == "__main__":
    if len(sys.argv) < 4 or sys.argv[1] == "":
        print("please input img path as first argument!")
        exit()

    img = loadImage(sys.argv[1])
    img = resizeImage(img, int(sys.argv[2]), int(sys.argv[3]) - 1)
    colors = processImage(img)

    outputColors(colors, img.size[0])
