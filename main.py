from sys import argv
from cv2 import imread, imshow, waitKey

from filter import *

if __name__ == "__main__":
    args = argv[2:]
    if not valid_arguments(args):
        filter_help()
        exit(1)

    input_img = imread(argv[1])
    imshow("input", input_img)

    output_img = input_img
    for i in args:
        f = filters[i]
        print(f"Applying '{' '.join(list(map(str.capitalize, (f.__name__.split('_')))))}'...")
        output_img = f(output_img)
    print("Done.")

    imshow("output", output_img)

    waitKey(0)
