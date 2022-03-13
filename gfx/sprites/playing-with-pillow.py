#!/usr/bin/env python3

# Author: Eddie Villasenor (edward.villasenor@gmail.com)

import sys

from PIL import Image

def print_image_to_terminal(region):
    px = region.load()
    for i in range(0,region.height,2): #for each row
        for j in range(region.width): #for each col
            l = px[j,i+1]
            u = px[j,i]
            lr, lg, lb = l[0], l[1], l[2]
            ur, ug, ub = u[0], u[1], u[2]
            print(f"\033[38;2;{lr};{lg};{lb}m" + # set foreground color
                    f"\033[48;2;{ur};{ug};{ub}m" + # set background color
                    "\N{LOWER HALF BLOCK}" + # unicode character printed
                    "\033[39m" + # reset foreground color
                    "\033[49m", # reset background color
                    end="")
        print()

def main():
    crop = False
    #imgpath = "./red.png"
    imgpath = sys.argv[1]
    im = Image.open(imgpath).convert('RGB')

    if crop:
        box = (1, 0, 15, 16)
        region = im.crop(box)
    else:
        region = im
    print_image_to_terminal(region)

if __name__=="__main__":
    main()
