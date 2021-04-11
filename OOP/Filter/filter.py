from os import system
from numpy import array, zeros, uint8
from cv2 import imread, imshow, getWindowProperty, WND_PROP_VISIBLE, waitKey, destroyAllWindows


def guide():
    print()

    system("figlet -c help")

    # TODO

    print()


class Image:
    def __init__(self, path: str):
        self.name = "Image"
        self.path: str = path
        self.image: array = imread(path)


class Apply:
    def __init__(self):
        self.Color = self.Color()
        self.Reflect = self.Reflect()
        self.Rotate = self.Rotate()
        self.Kernel = self.Kernel()

    class Color:
        def __init__(self):
            self.Grayscale = self.Grayscale()
            self.Sepia = self.Sepia()
            self.Inversion = self.Inversion()
            self.Sketch = self.Sketch()

        class Grayscale:
            def __init__(self, image: Image):
                image = image.image
                shape = image.shape

                output = zeros(shape, dtype=uint8)
                for i in range(shape[0]):
                    for j in range(shape[1]):
                        avg = sum(image[i][j]) / len(image[i][j])
                        output[i][j] = [avg] * 3

                self.name = "Grayscale"
                self.image = output

        class Sepia:
            def __init__(self, image: Image):
                image = image.image
                shape = image.shape

                output = zeros(shape, dtype=uint8)
                for i in range(shape[0]):
                    for j in range(shape[1]):
                        blue, green, red = image[i][j]
                        s_blue = min(255, .272 * red + .534 *
                                     green + .131 * blue)
                        s_green = min(255, .349 * red + .686 *
                                      green + .168 * blue)
                        s_red = min(255, .393 * red + .769 *
                                    green + .189 * blue)
                        output[i][j] = [int(s_blue), int(s_green), int(s_red)]

                self.name = "Sepia"
                self.image = output

        class Inversion:
            def __init__(self, image: Image):
                image = image.image
                shape = image.shape

                output = zeros(shape, dtype=uint8)
                for i in range(shape[0]):
                    for j in range(shape[1]):
                        output[i][j] = image[i][j][::-1]

                self.name = "Inversion"
                self.image = output

        class Sketch:
            def __init__(self, image: Image):
                image = image.image
                shape = image.shape

                output = zeros(shape, dtype=uint8)
                for i in range(shape[0]):
                    for j in range(shape[1]):
                        avg = sum(image[i][j]) / len(image[i][j])
                        if avg > 192:
                            output[i][j] = [255, 255, 255]
                        elif avg > 128:
                            output[i][j] = [170, 170, 170]
                        elif avg > 64:
                            output[i][j] = [85, 85, 85]
                        else:
                            output[i][j] = [0, 0, 0]

                self.name = "Sketch"
                self.image = output

    class Reflect:
        def __init__(self):
            self.Mirror = self.Mirror()
            self.Water = self.Water()

        class Mirror:
            def __init__(self, image: Image):
                image = image.image
                shape = image.shape

                output = zeros(shape, dtype=uint8)
                for i in range(shape[0]):
                    output[i] = image[i][::-1]

                self.name = "Mirror"
                self.image = output

        class Water:
            def __init__(self, image: Image):
                image = image.image

                output = image[::-1]

                self.name = "Water"
                self.image = output

    class Rotate:
        def __init__(self):
            self.Left = self.Left()
            self.Right = self.Right()

        class Left:
            def __init__(self, image: Image):
                image = image.image
                shape = image.shape

                output = zeros((shape[1], shape[0], shape[2]), dtype=uint8)
                for i in range(shape[1]):
                    for j in range(shape[0]):
                        output[i][j] = image[j][shape[1] - 1 - i]

                self.name = "Left"
                self.image = output

        class Right:
            def __init__(self, image: Image):
                image = image.image
                shape = image.shape

                output = zeros((shape[1], shape[0], shape[2]), dtype=uint8)
                for i in range(shape[1]):
                    for j in range(shape[0]):
                        output[i][shape[0] - 1 - j] = image[j][i]

                self.name = "Right"
                self.image = output

    class Kernel:
        def __init__(self):
            self.Blur = self.Blur()
            self.Edge = self.Edge()

        class Blur:
            def __init__(self, image: Image):
                image = image.image
                shape = image.shape

                output = zeros(shape, dtype=uint8)
                for i in range(shape[0]):
                    for j in range(shape[1]):
                        b_blue, b_green, b_red = 0, 0, 0
                        neighbors = 0
                        for m in range(-1, 2):
                            for n in range(-1, 2):
                                if 0 <= (i + m) < shape[0] and 0 <= (j + n) < shape[1]:
                                    b_blue += image[i + m][j + n][0]
                                    b_green += image[i + m][j + n][1]
                                    b_red += image[i + m][j + n][2]
                                    neighbors += 1
                        b_blue /= neighbors
                        b_green /= neighbors
                        b_red /= neighbors
                        output[i][j] = [int(b_blue), int(b_green), int(b_red)]

                self.name = "Blur"
                self.image = output

        class Edge:
            def __init__(self, image):
                image = image.image
                shape = image.shape
                gx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
                gy = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

                output = zeros(shape, dtype=uint8)
                for i in range(shape[0]):
                    for j in range(shape[1]):
                        ex_blue, ex_green, ex_red = 0, 0, 0
                        ey_blue, ey_green, ey_red = 0, 0, 0

                        for m in range(-1, 2):
                            for n in range(-1, 2):
                                if 0 <= (i + m) < shape[0] and 0 <= (j + n) < shape[1]:
                                    ex_blue += gx[m + 1][n + 1] * image[i + m][j + n][0]
                                    ex_green += gx[m + 1][n + 1] * image[i + m][j + n][1]
                                    ex_red += gx[m + 1][n + 1] * image[i + m][j + n][2]

                                    ey_blue += gy[m + 1][n + 1] * image[i + m][j + n][0]
                                    ey_green += gy[m + 1][n + 1] * image[i + m][j + n][1]
                                    ey_red += gy[m + 1][n + 1] * image[i + m][j + n][2]

                        e_blue = min(255, round((ex_blue ** 2 + ey_blue ** 2) ** 0.5))
                        e_green = min(255, round((ex_green ** 2 + ey_green ** 2) ** 0.5))
                        e_red = min(255, round((ex_red ** 2 + ey_red ** 2) ** 0.5))

                        output[i][j] = [int(e_blue), int(e_green), int(e_red)]

                self.name = "Edge"
                self.image = output


def show(any_filter):
    imshow(any_filter.name, any_filter.image)

    wait_time = 1000
    while getWindowProperty(any_filter.name, WND_PROP_VISIBLE) >= 1:
        key_code = waitKey(wait_time)
        if (key_code & 0xFF) == 27:
            destroyAllWindows()
            break
