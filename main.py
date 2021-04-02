from sys import argv
from cv2 import imread, imshow, waitKey

from filter import *

if __name__ == "__main__":
    filters = argv[2:]
    if not check_arguments(filters):
        filter_help()

    input_img = imread(argv[1])
    imshow("input", input_img)

    output_img = input_img
    for i in filters:
        output_img = apply_filter(output_img, i)
    imshow("output", output_img)

    waitKey(0)
