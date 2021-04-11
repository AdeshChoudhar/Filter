from os import system, listdir, path

from cv2 import imread, imwrite
from django.shortcuts import render, redirect
from numpy import zeros, uint8

from .forms import *

# Create your views here.
folder: str = "filter/static/filter/images"
inp_src: str
tmp_src: str
out_src: str


def index(request):
    return render(request, "filter/index.html", {"image_form": ImageForm()})


def apply(request):
    global folder
    global inp_src
    global tmp_src
    global out_src

    if request.method == 'POST':
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            system(f"rm -rf {folder}")
            image_form.save()

            file = list(listdir(folder))[0]
            extension = file.split(".")[1]
            system(f"mv {folder}/{file} {folder}/inp.{extension}")
            file = f"inp.{extension}"

            inp_src = path.join(folder, file)
            system(f"cp {inp_src} {folder}/tmp.{extension}")
            system(f"cp {inp_src} {folder}/out.{extension}")

            inp_src = f"{folder}/inp.{extension}"
            tmp_src = f"{folder}/tmp.{extension}"
            out_src = f"{folder}/out.{extension}"
            return render(request, "filter/apply.html", {"src": inp_src[6:]})
        else:
            return redirect("filter:index")
    return redirect("filter:index")


def grayscale(request):
    global tmp_src

    tmp_img = imread(tmp_src)
    shape = tmp_img.shape
    tmp_tmp = zeros(shape, dtype=uint8)
    for i in range(shape[0]):
        for j in range(shape[1]):
            avg = sum(tmp_img[i][j]) / len(tmp_img[i][j])
            tmp_tmp[i][j] = [avg] * 3

    imwrite(f"{tmp_src}", tmp_tmp)
    return render(request, "filter/apply.html", {"src": tmp_src[6:]})


def sepia(request):
    global tmp_src

    tmp_img = imread(tmp_src)
    shape = tmp_img.shape
    tmp_tmp = zeros(shape, dtype=uint8)
    for i in range(shape[0]):
        for j in range(shape[1]):
            blue, green, red = tmp_img[i][j]
            s_blue = min(255, .272 * red + .534 * green + .131 * blue)
            s_green = min(255, .349 * red + .686 * green + .168 * blue)
            s_red = min(255, .393 * red + .769 * green + .189 * blue)
            tmp_tmp[i][j] = [int(s_blue), int(s_green), int(s_red)]

    imwrite(f"{tmp_src}", tmp_tmp)
    return render(request, "filter/apply.html", {"src": tmp_src[6:]})


def inversion(request):
    global tmp_src

    tmp_img = imread(tmp_src)
    shape = tmp_img.shape
    tmp_tmp = zeros(shape, dtype=uint8)
    for i in range(shape[0]):
        for j in range(shape[1]):
            tmp_tmp[i][j] = tmp_img[i][j][::-1]

    imwrite(f"{tmp_src}", tmp_tmp)
    return render(request, "filter/apply.html", {"src": tmp_src[6:]})


def sketch(request):
    global tmp_src

    tmp_img = imread(tmp_src)
    shape = tmp_img.shape
    tmp_tmp = zeros(shape, dtype=uint8)
    for i in range(shape[0]):
        for j in range(shape[1]):
            avg = sum(tmp_img[i][j]) / len(tmp_img[i][j])
            if avg > 192:
                tmp_tmp[i][j] = [255, 255, 255]
            elif avg > 128:
                tmp_tmp[i][j] = [170, 170, 170]
            elif avg > 64:
                tmp_tmp[i][j] = [85, 85, 85]
            else:
                tmp_tmp[i][j] = [0, 0, 0]

    imwrite(f"{tmp_src}", tmp_tmp)
    return render(request, "filter/apply.html", {"src": tmp_src[6:]})


def mirror_reflection(request):
    global tmp_src

    tmp_img = imread(tmp_src)
    shape = tmp_img.shape
    tmp_tmp = zeros(shape, dtype=uint8)
    for i in range(shape[0]):
        tmp_tmp[i] = tmp_img[i][::-1]

    imwrite(f"{tmp_src}", tmp_tmp)
    return render(request, "filter/apply.html", {"src": tmp_src[6:]})


def water_reflection(request):
    global tmp_src

    tmp_img = imread(tmp_src)
    tmp_tmp = tmp_img[::-1]

    imwrite(f"{tmp_src}", tmp_tmp)
    return render(request, "filter/apply.html", {"src": tmp_src[6:]})


def rotate_left(request):
    global tmp_src

    tmp_img = imread(tmp_src)
    shape = tmp_img.shape
    tmp_tmp = zeros((shape[1], shape[0], shape[2]), dtype=uint8)
    for i in range(shape[1]):
        for j in range(shape[0]):
            tmp_tmp[i][j] = tmp_img[j][shape[1] - 1 - i]

    imwrite(f"{tmp_src}", tmp_tmp)
    return render(request, "filter/apply.html", {"src": tmp_src[6:]})


def rotate_right(request):
    global tmp_src

    tmp_img = imread(tmp_src)
    shape = tmp_img.shape
    tmp_tmp = zeros((shape[1], shape[0], shape[2]), dtype=uint8)
    for i in range(shape[1]):
        for j in range(shape[0]):
            tmp_tmp[i][shape[0] - 1 - j] = tmp_img[j][i]

    imwrite(f"{tmp_src}", tmp_tmp)
    return render(request, "filter/apply.html", {"src": tmp_src[6:]})


def blur(request):
    global tmp_src

    tmp_img = imread(tmp_src)
    shape = tmp_img.shape
    tmp_tmp = zeros(shape, dtype=uint8)
    for i in range(shape[0]):
        for j in range(shape[1]):
            b_blue, b_green, b_red = 0, 0, 0
            neighbors = 0
            for m in range(-1, 2):
                for n in range(-1, 2):
                    if 0 <= (i + m) < shape[0] and 0 <= (j + n) < shape[1]:
                        b_blue += tmp_img[i + m][j + n][0]
                        b_green += tmp_img[i + m][j + n][1]
                        b_red += tmp_img[i + m][j + n][2]
                        neighbors += 1
            b_blue /= neighbors
            b_green /= neighbors
            b_red /= neighbors
            tmp_tmp[i][j] = [int(b_blue), int(b_green), int(b_red)]

    imwrite(f"{tmp_src}", tmp_tmp)
    return render(request, "filter/apply.html", {"src": tmp_src[6:]})


def edge(request):
    global tmp_src

    tmp_img = imread(tmp_src)
    shape = tmp_img.shape
    tmp_tmp = zeros(shape, dtype=uint8)

    gx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    gy = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    for i in range(shape[0]):
        for j in range(shape[1]):
            ex_blue, ex_green, ex_red = 0, 0, 0
            ey_blue, ey_green, ey_red = 0, 0, 0

            for m in range(-1, 2):
                for n in range(-1, 2):
                    if 0 <= (i + m) < shape[0] and 0 <= (j + n) < shape[1]:
                        ex_blue += gx[m + 1][n + 1] * tmp_img[i + m][j + n][0]
                        ex_green += gx[m + 1][n + 1] * tmp_img[i + m][j + n][1]
                        ex_red += gx[m + 1][n + 1] * tmp_img[i + m][j + n][2]

                        ey_blue += gy[m + 1][n + 1] * tmp_img[i + m][j + n][0]
                        ey_green += gy[m + 1][n + 1] * tmp_img[i + m][j + n][1]
                        ey_red += gy[m + 1][n + 1] * tmp_img[i + m][j + n][2]

            e_blue = min(255, round((ex_blue ** 2 + ey_blue ** 2) ** 0.5))
            e_green = min(255, round((ex_green ** 2 + ey_green ** 2) ** 0.5))
            e_red = min(255, round((ex_red ** 2 + ey_red ** 2) ** 0.5))

            tmp_tmp[i][j] = [int(e_blue), int(e_green), int(e_red)]

    imwrite(f"{tmp_src}", tmp_tmp)
    return render(request, "filter/apply.html", {"src": tmp_src[6:]})


def home(request):
    return redirect("filter:index")


def save(request):
    global tmp_src
    global out_src

    tmp_img = imread(tmp_src)

    imwrite(f"{out_src}", tmp_img)
    return render(request, "filter/apply.html", {"src": tmp_src[6:]})


def download(request):
    global out_src

    system(f"cp {out_src} ~/Downloads/")
    return render(request, "filter/apply.html", {"src": tmp_src[6:]})
