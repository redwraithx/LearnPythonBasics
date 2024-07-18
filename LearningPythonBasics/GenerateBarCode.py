from PIL import Image

# install barcode using: pip install python-barcode
import barcode
from barcode.writer import ImageWriter

number = input("Enter the code to generate barcode 11 digits long (EX: 74934280394): ")
barcode_format = barcode.get_barcode_class('upc')
my_barcode = barcode_format(number, writer=ImageWriter())
my_barcode.save("generated_barcode")


Image.open('generated_barcode.png')