from django.shortcuts import render

# Create your views here.


def base(request):
    context = {
        "name": "Ankit",
    }
    return render(request, "todoApp/base.html", context)
