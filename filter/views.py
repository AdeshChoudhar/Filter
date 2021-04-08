from django.shortcuts import render, redirect
from .forms import *
from os import system, listdir, path


# Create your views here.
def index(request):
    return render(request, "filter/index.html", {"image_form": ImageForm()})


def apply(request):
    if request.method == 'POST':
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            folder = "filter/static/filter/images"
            system(f"rm -rf {folder}")
            image_form.save()
            file_name = list(listdir(folder))[0]
            src = path.join(folder, file_name)
            return render(request, "filter/apply.html", {"src": src[6:]})
        else:
            return redirect("filter:index")
    return redirect("filter:index")
