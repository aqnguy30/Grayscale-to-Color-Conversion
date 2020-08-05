import numpy as np
import cv2
import math
import random


class Coloring:

    def intensity_slicing(self, image, n_slices):
        # Convert greyscale image to color image using color slicing technique.
        # takes as input:
        # image: the grayscale input image
        # n_slices: number of slices

        # Steps:

        # 1. Split the exising dynamic range (0, k-1) using n slices (creates n+1 intervals)
        # 2. Randomly assign a color to each interval
        # 3. Create and output color image
        # 4. Iterate through the image and assign colors to the color image based on which interval the intensity belongs to

        # returns colored image

        final0 = np.zeros((np.shape(image)[0], np.shape(image)[1], 3))

        x = range(255)
        n = n_slices + 1
        num = float(len(x)) / n
        cutoff = [x[i:i + int(num)] for i in range(0, (n - 1) * int(num), int(num))]
        cutoff.append(x[(n - 1) * int(num):])
        #print(cutoff)

        colors = []
        for x in range(n):
            colors.append([random.randrange(256), random.randrange(256), random.randrange(256)])

        for x in range(0, np.shape(image)[0]):
            for y in range(0, np.shape(image)[1]):
                for k in range(0, len(cutoff)):
                    if image[x][y] <= cutoff[k][-1] and image[x][y] >= cutoff[k][0]:
                        final0[x][y] = colors[k]
        return final0

    def color_transformation(self, image, n_slices, theta):
        # Convert greyscale image to color image using color transformation technique.
        # takes as input:
        # image:  grayscale input image
        # colors: color array containing RGB values

        # Steps:
        # 1. Split the exising dynamic range (0, k-1) using n slices (creates n+1 intervals)
        # 2. create red values for each slice using 255*sin(slice + theta[0])
        #    similarly create green and blue using 255*sin(slice + theta[1]), 255*sin(slice + theta[2])
        # 3. Create and output color image
        # 4. Iterate through the image and assign colors to the color image based on which interval the intensity belongs to

        # returns colored image

        # return image

        final1 = np.zeros((np.shape(image)[0], np.shape(image)[1], 3))

        x = range(255)
        n = n_slices + 1
        num = float(len(x)) / n
        cutoff = [x[i:i + int(num)] for i in range(0, (n - 1) * int(num), int(num))]
        cutoff.append(x[(n - 1) * int(num):])
        #print(cutoff)

        colors = []
        for x in range(0, len(cutoff)):
            colors.append([255 * math.sin((((min(cutoff[x]) + max(cutoff[x])) / 2) + theta[0]) * math.pi / 180),
                           255 * math.sin((((min(cutoff[x]) + max(cutoff[x])) / 2) + theta[1]) * math.pi / 180),
                           255 * math.sin((((min(cutoff[x]) + max(cutoff[x])) / 2) + theta[2]) * math.pi / 180)])

        for x in range(0, np.shape(image)[0]):
            for y in range(0, np.shape(image)[1]):
                for k in range(0, len(cutoff)):
                    if image[x][y] <= cutoff[k][-1] and image[x][y] >= cutoff[k][0]:
                        final1[x][y] = colors[k]
                        #Uncomment the below part if we want the background to be black:
                        #if k == 0:
                            #final1[x][y] = [0,0,0]
        return final1
