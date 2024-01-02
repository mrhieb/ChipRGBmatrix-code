#!/usr/bin/env python
import time
from samplebase import SampleBase
from PIL import Image


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
            

# Main function
# e.g. call with
#  sudo ./image-scroller.py --chain=4
# if you have a chain of four
if __name__ == "__main__":
    image_scroller = ImageShow('square.png')
    if (not image_scroller.process()):
        image_scroller.print_help()

