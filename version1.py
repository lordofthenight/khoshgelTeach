import PIL
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
ADDRESS = "/home/hossein/Documents/GitHub/khoshgelTeach/FarsiAlphImages/"
pic1 = 'alef.jpg'


letter=input("Please enter your letter: ")
if letter == 'a' or letter == 'A':
	img_1 = Image.open(ADDRESS+pic1)
	img_1.show()	


