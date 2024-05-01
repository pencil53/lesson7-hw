import cv2
import os
import PIL
from PIL import Image

#pillow = image processing library

path = "images"
meanwidth = 0
meanheight = 0
files = os.listdir(path)
num_of_images = len(files)

for file in files:
    image = Image.open(os.path.join(path,file))
    width,height = image.size
    meanwidth = meanwidth + width
    meanheight = meanheight + height

meanwidth = meanwidth//num_of_images
meanheight = meanheight//num_of_images


for file in files:
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
        image = Image.open(os.path.join(path,file))
        imageresized = image.resize((meanwidth,meanheight), PIL.Image.Resampling.LANCZOS)
        newpath = os.path.join(path,file)
        imageresized.save(newpath, "JPEG", quality = 95)
        print("image resized")

def videogenerator():
    videoname = "MyFirstVideohw.avi"
    images = []
    for img in os.listdir(path):
        if img.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
            images.append(img)
    frame = cv2.imread(os.path.join(path,images[0]))
    height,width,layers = frame.shape
    video_writer = cv2.VideoWriter(videoname,0,1,(width,height))
    for img in images:
        video_writer.write(cv2.imread(os.path.join(path,img)))
    cv2.destroyAllWindows()
    video_writer.release()
videogenerator()