from sys import argv
from cv2 import imread, imshow, getWindowProperty, WND_PROP_VISIBLE, waitKey, destroyAllWindows

from filter import *

if __name__ == "__main__":
    args = argv[2:]
    if not valid_arguments(args):
        guide()
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

    wait_time = 1000
    while getWindowProperty("output", WND_PROP_VISIBLE) >= 1:
        key_code = waitKey(wait_time)
        if (key_code & 0xFF) == 27:
            destroyAllWindows()
            break
