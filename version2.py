import PIL
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
ADDRESS = "/home/hossein/Documents/GitHub/khoshgelTeach/FarsiAlphImages/"
img_1 = 'alef.jpg'
img_2 = 'be.jpg'
img_3 = 'pe.jpg'
img_4 = 'te.jpg'
img_5 = 'th.jpg'
img_6 = 'je.jpg'
img_7 = 'che.jpg'
img_8 = 'ha.jpg'
img_9 = 'kh.jpg'
img_10 = 'de.jpg'
img_11 = 'ze.jpg'
img_12 = 'ce.jpg'

####function######

letter=input("Please enter your letter: ")
if letter == 'a' or letter == 'A':
	img_1 = Image.open(ADDRESS+img_1)
	img_1.show()
elif letter == 'b' or letter == 'B':
	img_2 = Image.open(ADDRESS+img_2)
	img_2.show()
elif letter == 'p' or letter == 'P':
	img_3 = Image.open(ADDRESS+img_3)
	img_3.show()
elif letter == 't' or letter == 'T':
	img_4 = Image.open(ADDRESS+img_4)
	img_4.show()
elif letter == 'th' or letter == 'TH':
	img_5 = Image.open(ADDRESS+img_5)
	img_5.show()
elif letter == 'j' or letter == 'J':
	img_6 = Image.open(ADDRESS+img_6)
	img_6.show()
elif letter == 'ch' or letter == 'CH':
	img_7 = Image.open(ADDRESS+img_7)
	img_7.show()
elif letter == 'h' or letter == 'H':
	img_8 = Image.open(ADDRESS+img_8)
	img_8.show()
elif letter == 'kh' or letter == 'KH':
	img_9 = Image.open(ADDRESS+img_9)
	img_9.show()
elif letter == 'd' or letter == 'D':
	img_10 = Image.open(ADDRESS+img_10)
	img_10.show()
elif letter == 'z' or letter == 'Z':
	img_11 = Image.open(ADDRESS+img_11)
	img_11.show()
elif letter == 'c' or letter == 'C':
	img_12 = Image.open(ADDRESS+img_12)
	img_12.show()
	
