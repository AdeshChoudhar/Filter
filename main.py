import cv2 as cv

from filter import *

if __name__ == "__main__":
    input_img = cv.imread("images/stadium.bmp")
    cv.imshow("input", input_img)

    grayscale_img = grayscale(input_img)
    cv.imshow("grayscale", grayscale_img)

    sepia_img = sepia(input_img)
    cv.imshow("sepia", sepia_img)

    mirror_reflection_img = mirror_reflection(input_img)
    cv.imshow("mirror_reflection", mirror_reflection_img)

    water_reflection_img = water_reflection(input_img)
    cv.imshow("water_reflection", water_reflection_img)

    rotate_left_img = rotate_left(input_img)
    cv.imshow("rotate_left", rotate_left_img)

    rotate_right_img = rotate_right(input_img)
    cv.imshow("rotate_right", rotate_right_img)

    bgr_to_rgb_img = bgr_to_rgb(input_img)
    cv.imshow("bgr_to_rgb", bgr_to_rgb_img)

    blur_img = blur(input_img)
    cv.imshow("blur", blur_img)

    cv.waitKey(0)
