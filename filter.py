from numpy import zeros, uint8

from helpers import *


def valid_arguments(args):
    filter_arguments = list(filters.keys())

    if (args == []):
        return False

    for i in args:
        if i not in filter_arguments:
            return False
    return True


def grayscale(inp):
    shape = inp.shape
    out = zeros(shape, dtype=uint8)
    for i in range(shape[0]):
        for j in range(shape[1]):
            avg = sum(inp[i][j]) / len(inp[i][j])
            out[i][j] = [avg] * 3
    return out


def sepia(inp):
    shape = inp.shape
    out = zeros(shape, dtype=uint8)
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
    out = zeros(shape, dtype=uint8)
    for i in range(shape[0]):
        out[i] = inp[i][::-1]
    return out


def water_reflection(inp):
    out = inp[::-1]
    return out


def rotate_left(inp):
    shape = inp.shape
    out = zeros((shape[1], shape[0], shape[2]), dtype=uint8)
    for i in range(shape[1]):
        for j in range(shape[0]):
            out[i][j] = inp[j][i]
    return out


def rotate_right(inp):
    shape = inp.shape
    out = zeros((shape[1], shape[0], shape[2]), dtype=uint8)
    for i in range(shape[1]):
        for j in range(shape[0]):
            out[i][shape[0] - 1 - j] = inp[j][i]
    return out


def colour_inversion(inp):
    shape = inp.shape
    out = zeros(shape, dtype=uint8)
    for i in range(shape[0]):
        for j in range(shape[1]):
            out[i][j] = inp[i][j][::-1]
    return out


def blur(inp):
    shape = inp.shape
    out = zeros(shape, dtype=uint8)
    for i in range(shape[0]):
        for j in range(shape[1]):
            b_blue, b_green, b_red = 0, 0, 0
            neighbors = 0
            for m in range(-1, 2):
                for n in range(-1, 2):
                    if 0 <= (i + m) < shape[0] and 0 <= (j + n) < shape[1]:
                        b_blue += inp[i + m][j + n][0]
                        b_green += inp[i + m][j + n][1]
                        b_red += inp[i + m][j + n][2]
                        neighbors += 1
            b_blue /= neighbors
            b_green /= neighbors
            b_red /= neighbors
            out[i][j] = [int(b_blue), int(b_green), int(b_red)]
    return out


filters = {
    "-gs": grayscale,
    "-sp": sepia,
    "-wr": water_reflection,
    "-mr": mirror_reflection,
    "-rl": rotate_left,
    "-rr": rotate_right,
    "-ci": colour_inversion,
    "-bl": blur,
}
