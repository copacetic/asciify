from PIL import Image
from PIL import ImageOps
from PIL import ImageStat

import math

box_side = 6
im = Image.open("cat.jpg")
gray_im = ImageOps.grayscale(im)
the_string = ''

image_width = gray_im.size[0]
image_height = gray_im.size[1]

pixels = gray_im.getdata()

# 32 to 126 range in ascii
px_val_to_ascii_char_map = {}
for char_code_bucket in range(0, 32*8):
    char_code = (char_code_bucket -  (char_code_bucket % 8)) / 8
    px_val_to_ascii_char_map[char_code_bucket] = str(unichr(char_code + 32))

bottom_right_x = box_side
top_left_x = 0
top_left_y = 0
bottom_right_y = box_side
while bottom_right_y < image_height:
    in_bounds_x = True
    top_left_x = 0
    bottom_right_x = box_side
    while bottom_right_x < image_width:
        window = im.crop((top_left_x, top_left_y, bottom_right_x, bottom_right_y))
        mean_px_value = math.floor(ImageStat.Stat(window).mean[0])
        ascii_char = px_val_to_ascii_char_map[mean_px_value]
        the_string += ascii_char
        top_left_x += box_side
        bottom_right_x += box_side
        if bottom_right_x >= image_width:
            the_string += '\r\n';
    top_left_y += box_side
    bottom_right_y += box_side

print the_string
