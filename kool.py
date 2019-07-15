'''
MIT License

Copyright (c) 2019 zacreid

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import random, numpy
from PIL import Image, ImageFilter

colors = numpy.load("colors.npy")
colorstwo = colors.reshape(12,18,3)
colorsthree = [[[55,55,55],[55,25,65]],[[55,255,0],[25,125,60]],[[255,54,255],[225,45,255]]]
colorsfour = [[[221, 252, 173]],[[200, 224, 135]],[[149, 164, 114]],[[130, 132, 109]],[[100, 97, 101]]]
colorsfive = [[[166, 58, 80]],[[240, 231, 216]],[[171, 155, 150]],[[161, 103, 74]],[[186, 110, 110]]]
colorssix = [[[95, 112, 95]],[[239, 118, 122]],[[125, 122, 188]],[[100, 87, 166]],[[255, 227, 71]]]
colorsseven = [[[255,255,255]],[[251, 194, 181]],[[255, 168, 169]],[[247, 134, 170]],[[161, 74, 118]],[[255, 118, 118], [255, 95, 118]]]
colorsseven = colorsseven[::-1]

kolor = [colorstwo, colorsthree, colorsfour, colorsfive, colorssix, colorsseven]

def mono_color(image, colorwhite, colorblack, blocky=3):
  if isinstance(image, str):
    image = Image.open(image)
  image = image.convert('1').filter(ImageFilter.ModeFilter)
  size = image.size
  if blocky > 1:
    image = image.resize((size[0]/blocky, size[1]/blocky)).resize((size[0], size[1]))

  def addColor(x):
    if x:
      return random.choice(colorwhite)
    return random.choice(colorblack)

  image = numpy.array(image)
  image = image.reshape(size[1] * size[0], 1)

  arr = numpy.array(map(addColor, image))
  arr = arr.reshape(size[1], size[0], 3)

  return Image.fromarray(arr.astype(numpy.uint8))


def cool_color(image, colors, blocky=3):
  if isinstance(image, str):
    image = Image.open(image)
  image = image.convert('L').filter(ImageFilter.ModeFilter)
  size = image.size
  if blocky > 1:
    image = image.resize((size[0]/blocky, size[1]/blocky)).resize((size[0], size[1]))

  lcolors = len(colors)
  divide = 255 / lcolors
  new = []
  for x in range(lcolors):
    new += [x]*divide
  new += [x]*(256 - len(new))

  def addColor(x, colors=colors, new=new):
    return random.choice(colors[new[x[0]]])

  image = numpy.array(image)
  image = image.reshape(size[1] * size[0], 1)

  arr = numpy.array(map(addColor, image))
  arr = arr.reshape(size[1], size[0], 3)

  return Image.fromarray(arr.astype(numpy.uint8)).resize((size[0], size[1]))
