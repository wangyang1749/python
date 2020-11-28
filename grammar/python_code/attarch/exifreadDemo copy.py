
import exifread
import json
import urllib.request
 
# Open image file for reading (binary mode)
f = open("/home/wy/source_code/opencv_opengl/python_code/attarch/01.jpg", 'rb')
 
# Return Exif tags
tags = exifread.process_file(f)
print(tags['GPS GPSLatitudeRef'],tags['GPS GPSLongitudeRef'],tags['GPS GPSTimeStamp'],tags['GPS GPSDate'])

print(tags['Image GPSInfo'])