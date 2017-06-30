from slovnik.models import RatingImages
import os
from PIL import Image
from random import randint

def load_images():
    path = 'C:/Users/Honza/PycharmProjects/logopedia/media/'
    in_load = 'tmp_images/'
    out_save = 'rating_images/'
    namestr = 'abcdefghijklmnopqrstuvwxyz1234567890'
    height = 450
    for file in os.listdir(path+in_load):
        filename = os.fsdecode(file)

        outfile = ''
        for i in range(0, 8):
            outfile += namestr[randint(0, len(namestr)-1)]

        im = Image.open(path+in_load+filename)
        print(filename)
        width = int(im.size[0]*height/im.size[1])
        im.thumbnail((width, height))
        im.save(path+out_save+outfile+'.jpg', "JPEG")
        RatingImages.objects.create(name=outfile, image=out_save+outfile+'.jpg')

