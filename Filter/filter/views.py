from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def index(request):
    return render(request, "filter/index.html", {"image_form": ImageForm()})


def apply(request):
    if request.method == 'POST':
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image_form.save()
            return render(request, "filter/apply.html")
        else:
            return redirect("filter:index")
    return redirect("filter:index")
