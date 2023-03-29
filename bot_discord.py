from PIL import Image
import os

downloadsFolder = r"/Users/jusus/Downloads/Example4/FDownload
files = os.listdir(downloadsFolder)

picturesFolder = r"/Users/jusus/Downloads/Example4/FDownload
videoFolder = r"/Users/jusus/Downloads/Example4/FDownload
picturesFolder= r"/Users/jusus/Downloads/Example4/FDownload

if _name_ == "_main_":
    for filename in files:
        name,extension = os.path.splitext(downloadsFolder+filename)
        if extension in [".jpg", ".png", ".jpeg"]:
            picture=Image.open(downloadsFolder+filename)
            picture.save(downloadsFolder+'compressed_'+filename, optimize=True, quality=60)
            os.remove(downloadsFolder+filename)

        if extension in [".mp3"]:
        os.rename(downloadsFolder + filename, audioFolder)
        if extension in [".mp4"]:
        os.rename(downloadsFolder + filename, audioFolder)