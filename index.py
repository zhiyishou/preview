from PIL import Image

def resizeImage(im, width, height):
    originalW, originalH = im.size
    originalRatio = originalW / originalH
    ratio = width / height

    newW, newH = int(width), int(height)

    if (ratio < originalRatio):
        newH = int(width / originalRatio)
    else:
        newW = int(height * originalRatio)

    return im.resize((newW, newH), Image.ANTIALIAS)

def loadImage(path):
    try:
        return Image.open(path)
    except FileNotFoundError:
        print("There is no such image exits.")

if __name__ == "__main__":
    img = loadImage("./img/mao.jpg")
    # print(len(list(resizeImage(img, 100, 100).getdata())))
    img = resizeImage(img, 100, 100)
    print(img.size)
