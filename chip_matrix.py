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
        
class ImageShow(SampleBase):
    def __init__(self, image, *args, **kwargs):
        super(ImageShow, self).__init__(*args, **kwargs)
        self.parser.add_argument("-i", "--image", help="The image to display", default = image)

    def run(self):
        if not 'image' in self.__dict__:
            self.image = Image.open(self.args.image).convert('RGB')
        double_buffer = self.matrix.CreateFrameCanvas()
        double_buffer.SetImage(self.image, 0)
        double_buffer = self.matrix.SwapOnVSync(double_buffer)




class SetMatrix(SampleBase):
    def __init__(self, x, y, mat, x_mat, y_mat,  *args, **kwargs):
        super(SetMatrix, self).__init__(*args, **kwargs)
        self.x = x
        self.y = y
        self.mat = mat
        self.x_mat = x_mat
        self.y_mat = y_mat

    def run(self):
        canvas = self.matrix
        number = 0
        level = 0
        for i in self.mat:
            self.matrix.SetPixel(self.x+number, self.y+level, i[0], i[1], i[2])
            
            number = number + 1
            if number>=self.x_mat:
                number= 0
                level = level+1

class SetText(SampleBase):
    def __init__(self, x, y, words, red, green, blue, font_size, *args, **kwargs):
        super(SetText, self).__init__(*args, **kwargs)
        self.words = words
        self.red = red
        self.green = green
        self.blue = blue
        self.x = x
        self.y = y
        self.font_size =font_size
    def run(self):
        canvas = self.matrix
        font = graphics.Font()
        if self.font_size == 'tiny':
            font.LoadFont("../../../fonts/4x6.bdf")
        if self.font_size == 'small':
            font.LoadFont("../../../fonts/6x9.bdf")
        if self.font_size == 'medium':
            font.LoadFont("../../../fonts/7x13.bdf")
        if self.font_size == 'large':
            font.LoadFont("../../../fonts/9x15.bdf")
        if self.font_size == 'huge':
            font.LoadFont("../../../fonts/10x20.bdf")
        color = graphics.Color(self.red, self.green, self.blue)
        graphics.DrawText(canvas, font,self.x, self.y, color, self.words)
        
# Main function
if __name__ == "__main__":
    graphics_test = SetPixel(20, 10, 255, 255, 0)
    if (not graphics_test.process()):
        graphics_test.print_help()


