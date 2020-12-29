import matplotlib
from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import image as mpimg
from matplotlib.pyplot import figure
import numpy as np

import cv2

def blackAndWhite(imagepath):
	img = np.array(mpimg.imread(imagepath,0)) #replace this with your path of image
	img_color = img

	# num_down =  2
	# num_bilateral = 7 

	# # downsample image using Gaussian pyramid(see opencv 'pyrDown()' function)
	# for _ in range(num_down):
	#     img_color = cv2.pyrDown(img_color)

	# # repeatedly apply small bilateral filter instead of applying one large filter
	# for _ in range(num_bilateral):
	#     img_color = cv2.bilateralFilter(img_color, 9, 9, 7)

	# # upsample image to original size (see opencv 'pyrUp()' function)
	# for _ in range(num_down):
	#     img_color = cv2.pyrUp(img_color)


	img_gray = cv2.cvtColor(img_color, cv2.COLOR_RGB2GRAY)
	# img_blur = cv2.medianBlur(img_gray, 7)

	# img_edge = cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,9,2)

	# img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)

	# final =  cv2.bitwise_and(img_color,img_edge)
	return img_gray


