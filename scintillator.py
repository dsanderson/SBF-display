from samplebase import SampleBase
from rgbmatrix import graphics
import itertools
import time, random


class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)
        self.gen_pixel_list()
        canvas = self.matrix
        self.draw_start()
        self.run()

    def gen_pixel_list(self):
        panels =
        self.pixels = []
        for p in panels:
            xmin, xmax, ymin, ymax = get_bounds(p)
            base_color = p[]
            pixels = list(itertools.product(range(xmin, xmax), range(ymin, ymax)))
            pixels = [transform_pixel(pix) for pix in pixels]
            pixels = [(pix, base_color) for pix in pixels]
            self.pixels.append(pixels)

    def randomize_color(self, col):
        shift = random.randint(-10, 10)
        r = col[0]+shift if col[0]+shift<255 else 255
        g = col[1]+shift if col[1]+shift<255 else 255
        b = col[2]+shift if col[2]+shift<255 else 255
        return r,g,b

    def draw_start(self):
        for p in self.pixels:
            r,g,b = p[1]
            graphics.SetPixel(p[0][0], p[0][1], r, g, b)

    def run(self):
        #font = graphics.Font()
        #font.LoadFont("../../fonts/7x13.bdf")
        changed_pixels_indecies = []
        while True:
            i = random.randint(0, len(self.pixels))
            if len(changed_pixels_indecies)>100:
                i0 = changed_pixels_indecies.pop(0)
                r, g, b = self.pixels[i0][1]
                graphics.SetPixel(self.pixels[i0][0][0], self.pixels[i0][0][1], r, g, b)
            r, g, b = randomize_color(self.pixels[i][1])
            graphics.SetPixel(self.pixels[i][0][0], self.pixels[i][0][1], r, g, b)
            changed_pixels_indecies.push(i)
