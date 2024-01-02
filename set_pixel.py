#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time

from PIL import Image

class SetPixel(SampleBase):
    def __init__(self, x, y, red, green, blue, *args, **kwargs):
        super(SetPixel, self).__init__(*args, **kwargs)
        self.x = x
        self.y = y
        self.red = red
        self.green = green
        self.blue = blue

    def run(self):
        canvas = self.matrix
        self.matrix.SetPixel(self.x, self.y, self.red, self.green, self.blue)
        

    
# Main function
if __name__ == "__main__":
    graphics_test = SetPixel(20, 10, 255, 255, 0)
    if (not graphics_test.process()):
        graphics_test.print_help()

