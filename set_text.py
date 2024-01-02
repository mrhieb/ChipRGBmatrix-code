#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time


class GraphicsTest(SampleBase):
    def __init__(self, x, y, words, red, green, blue, font_size, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)
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
    graphics_test = GraphicsTest(0, 15,'Welcome', 128, 128, 0, 'large')
    if (not graphics_test.process()):
        graphics_test.print_help()

