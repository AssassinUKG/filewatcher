import pyimgur
from pathlib import Path

clientID = '03945b7e998cc46'

def UploadtoImgur(filep):
    im = pyimgur.Imgur(clientID)
    retImg = im.upload_image(filep, title="Work")
    print(retImg.link)
    return(retImg.link)


#Basic Usage

#  x = UploadtoImgur(pathToImg)
#  print(x)

#Imgur ID: 03945b7e998cc46
#Imgur Secret: b800493a2f9c43e3c153f95a241a71c5f3a2c3a3


#UploadtoImgur(r"C:\\Users\\richa\Desktop\screen.PNG")