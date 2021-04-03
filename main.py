from sys import argv
from cv2 import imread, imshow, waitKey

from filters import *

if __name__ == "__main__":
    filters = argv[2:]
    if not check_arguments(filters):
        filter_help()

    input_img = imread(argv[1])
    imshow("input", input_img)

    output_img = input_img
    for i in filters:
        f = get_filter(i)
        print(f"Applying '{' '.join(list(map(str.capitalize, (f.__name__.split('_')))))}'...")
        output_img = f(output_img)
    print("Done.")

    imshow("output", output_img)

    waitKey(0)
