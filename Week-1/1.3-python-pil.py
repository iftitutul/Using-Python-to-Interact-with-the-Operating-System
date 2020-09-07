#!/usr/bin/env python3

import PIL.Image
image = PIL.Image.open("aws.png")

print (image.size)
print (image.format)