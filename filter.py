import numpy as np


def grayscale(inp):
    shape = inp.shape
    out = np.zeros(shape, dtype=np.uint8)
    for i in range(shape[0]):
        for j in range(shape[1]):
            avg = sum(inp[i][j]) / len(inp[i][j])
            out[i][j] = [avg] * 3
    return out


def sepia(inp):
    shape = inp.shape
    out = np.zeros(shape, dtype=np.uint8)
    for i in range(shape[0]):
        for j in range(shape[1]):
            blue, green, red = inp[i][j]
            s_blue = min(255, .272 * red + .534 * green + .131 * blue)
            s_green = min(255, .349 * red + .686 * green + .168 * blue)
            s_red = min(255, .393 * red + .769 * green + .189 * blue)
            out[i][j] = [int(s_blue), int(s_green), int(s_red)]
    return out


def mirror_reflection(inp):
    shape = inp.shape
    out = np.zeros(shape, dtype=np.uint8)
    for i in range(shape[0]):
        out[i] = inp[i][::-1]
    return out


def water_reflection(inp):
    shape = inp.shape
    out = inp[::-1]
    return out


def rotate_left(inp):
    shape = inp.shape
    out = np.zeros((shape[1], shape[0], shape[2]), dtype=np.uint8)
    for i in range(shape[1]):
        for j in range(shape[0]):
            out[i][j] = inp[j][i]
    return out


def rotate_right(inp):
    shape = inp.shape
    out = np.zeros((shape[1], shape[0], shape[2]), dtype=np.uint8)
    for i in range(shape[1]):
        for j in range(shape[0]):
            out[i][shape[0] - 1 - j] = inp[j][i]
    return out


def bgr_to_rgb(inp):
    shape = inp.shape
    out = np.zeros(shape, dtype=np.uint8)
    for i in range(shape[0]):
        for j in range(shape[1]):
            out[i][j] = inp[i][j][::-1]
    return out


def blur(inp):
    shape = inp.shape
    out = np.zeros(shape, dtype=np.uint8)
    for i in range(shape[0]):
        for j in range(shape[1]):
            b_blue, b_green, b_red = 0, 0, 0
            neighbors = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if 0 <= (i + k) < shape[0] and 0 <= (j + l) < shape[1]:
                        b_blue += inp[i + k][j + l][0]
                        b_green += inp[i + k][j + l][1]
                        b_red += inp[i + k][j + l][2]
                        neighbors += 1
            b_blue /= neighbors
            b_green /= neighbors
            b_red /= neighbors
            out[i][j] = [int(b_blue), int(b_green), int(b_red)]
    return out
