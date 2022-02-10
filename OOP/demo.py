from Filter import filter

image = filter.Image("../media/input.bmp")

color = filter.Apply.Color
reflect = filter.Apply.Reflect
rotate = filter.Apply.Rotate
kernel = filter.Apply.Kernel

grayscale = color.Grayscale(image)
# sepia = color.Sepia(image)
# inversion = color.Inversion(image)
# sketch = color.Sketch(image)
#
# mirror = reflect.Mirror(image)
# water = reflect.Water(image)
#
# left = rotate.Left(image)
# right = rotate.Right(image)
#
# blur = kernel.Blur(image)
# edge = kernel.Edge(image)

filter.show(grayscale)
# filter.show(sepia)
# filter.show(inversion)
# filter.show(sketch)
#
# filter.show(mirror)
# filter.show(water)
#
# filter.show(left)
# filter.show(right)

# filter.show(blur)
# filter.show(edge)
