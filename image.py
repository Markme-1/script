#!/usr.bin.python
from PIL import Image

location = input("enter path/filename: ")

image = Image.open(location)

#print("Original size : {image.size}") # 5464x3640

x = int(input("x: "))
y = int(input("y: "))

sunset_resized = image.resize((x, y))

output = input("output file name : ")

#sunset_resized.save("m" + location)
sunset_resized.save(output)
