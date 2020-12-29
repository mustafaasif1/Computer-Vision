import matplotlib
from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import image as mpimg
from matplotlib.pyplot import figure
import numpy as np

import cv2

def cartoonifier(imagepath):
	img = np.array(mpimg.imread(imagepath,0)) #replace this with your path of image
	img_copy = img

	num_down =  3
	num_bilateral = 10

	# downsample image using Gaussian pyramid(see opencv 'pyrDown()' function)
	for num in range(num_down):
	    img_copy = cv2.pyrDown(img_copy)

	# repeatedly apply small bilateral filter instead of applying one large filter
	for num in range(num_bilateral):
	    img_copy = cv2.bilateralFilter(img_copy, 9, 10, 8)

	# upsample image to original size (see opencv 'pyrUp()' function)
	for num in range(num_down):
	    img_copy = cv2.pyrUp(img_copy)

	blackAndWhite_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	blurred_img = cv2.medianBlur(blackAndWhite_img, 7)
	edge_of_img = cv2.adaptiveThreshold(blurred_img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,9,2)
	edge_of_img = cv2.cvtColor(edge_of_img, cv2.COLOR_GRAY2RGB)
	final = cv2.bitwise_and(img,edge_of_img)
	return final