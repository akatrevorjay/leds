from __future__ import absolute_import, division, print_function

import itertools
from math import sin, pi

import mpsse
from Adafruit_NeoPixel_FTDI import Adafruit_NeoPixel


n = (56 * 8)
#n = 480

gamma = 2.75
brightness = 0.05
# brightness = 1

low = 1
high = 255

tau = 2 * pi


def convert(x):
   # Input in range 0 - 1, output in range 0-255
   return int(x ** gamma * 254) + 1
   # return int(x * 255)


def gradient(length=n):
   for i in range(length):
       x = i / length
       yield x, x, x


def sine(t, x, speed=1.0, wavelength=80):
   v = 0.5 + 0.5 * sin((x - speed*t) * (tau / wavelength))
   return v


def convert_color(c):
   r, g, b = c
   return convert(r), convert(g), convert(b)


def main():
    inst = Adafruit_NeoPixel(n)
    inst.setBrightness(brightness)

    for t in itertools.count():
        for x in range(n):
            r = sine(t, x, speed=1)
            g = sine(t, x, speed=0.5, wavelength=160)
            b = sine(t, x, speed=-1)

            rgb = convert_color([r, g, b])

            inst.setPixelColorRGB(x, *rgb)
        inst.show()


if __name__ == '__main__':
    main()
