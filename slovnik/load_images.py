from slovnik.models import RatingImages
import os


def load_images():
    path = '/home/honza/PycharmProjects/logopedia/media/rating_images'
    for file in os.listdir(path):
        filename = os.fsdecode(file)
        print(filename)
        RatingImages.objects.create(image=filename, upload_to='rating_images')
