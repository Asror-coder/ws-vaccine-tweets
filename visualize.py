#!/usr/bin/env python3
import base64
import os
import sys
import yaml
from PIL import Image
from io import BytesIO


def vaccine_polarity_visualisation(vaccine):
    # with open("/data/"+vaccine+"_timeseries_polarity_optimised_dataset.png", "rb") as image_file:
    #     encoded_string = base64.b64encode(image_file.read())
    # print(encoded_string.decode('utf-8'))
    # image = Image.open(BytesIO(base64.b64decode(encoded_string)))
    # return image
    # image.show()
    im = Image.open('/data/covaxin_timeseries_polarity_optimised_dataset.png')
    im.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # vaccine = input("Please enter vaccine name for which you want the sentiment analysis visualisation: \n")
    # vaccine_polarity_visualisation(vaccine)

    # Make sure that at least one argument is given, that is either 'encode' or 'decode'
    # if len(sys.argv) != 2:
    #     print(f"Usage: {sys.argv[0]} Please enter vaccine name for which you want the sentiment analysis computation:")
    #     exit(1)

    # If it checks out, call the appropriate function
    command = sys.argv[1]
    # result=vaccine_polarity_visualisation(os.environ["INPUT"])
    vaccine_polarity_visualisation(os.environ["INPUT"])
    # Print the result with the YAML package
    print(yaml.dump({ "output": 'I am visualization' }))