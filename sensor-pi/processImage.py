
import sys;
from cv import *;
import getopt;

# Resizes the image
def resizeImage(rootdir, filename, prefixString, resizeFactor):

    # Loads the original image
    original_img = LoadImage(rootdir + filename)

    # Creates a destination image
    img = CreateImage(GetSize(original_img), 8, 1)

    # Convert the image to gray_scale
    CvtColor(original_img, img, CV_RGB2GRAY);
    size = GetSize(img)

    # Set up the resized image size
    newImage = CreateImage(( size[0] / resizeFactor, size[1] / resizeFactor), img.depth, img.nChannels)

    # Resize the image
    Resize(img, newImage)
    size = GetSize(newImage)

    # Crop the image
    newImage = newImage[size[1]/3:4*(size[1]/5), 0:]

    # Write the image to files
    SaveImage(prefixString + filename, newImage)


# Gets the appropriate command line arguments
def getCommandLineArguments():
    filename = ""
    prefixString = ""
    try:
        opts, args = getopt.getopt(sys.argv[1:], "n:p:", ["name=", "prefix="])
    except getopt.GetoptError:
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-n", "-name"):
            filename = arg
        elif opt in ("-p", "-prefix"):
            prefixString = arg

    return filename, prefixString
    
           
rootDirectory = ""
resizeFactor = 3

filename, prefixString = getCommandLineArguments()

resizeImage(rootDirectory, filename, prefixString, resizeFactor)

