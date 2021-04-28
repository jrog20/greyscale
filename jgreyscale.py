"""
File: greyscale.py
----------------
This program turns a color photo to black and white.
"""

from simpleimage import SimpleImage

def main():
    original_peri = SimpleImage('images/peri.jpg')
    original_peri.show()

    greyscale_peri = greyscale('images/peri.jpg')
    greyscale_peri.show()

def compute_luminosity(red, green, blue):
    """
      Calculates the luminosity of a pixel using NTSC formula
      to weight red, green, and blue values appropriately.
      """
    return (0.299 * red) + (0.587 * green) + (0.114 * blue)

def greyscale(filename):
    """
     Reads image from file specified by filename.
     Change the image to be grayscale using the NTSC
     luminosity formula and return it.
     """
    image = SimpleImage(filename)
    for pixel in image:
        luminosity = compute_luminosity(pixel.red, pixel.green, pixel.blue)
        pixel.red = luminosity
        pixel.green = luminosity
        pixel.blue = luminosity
    return image

if __name__ == '__main__':
    main()
