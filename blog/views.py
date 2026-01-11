from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})


def detalle_list(request):
    return render(request, 'blog/detalle.html', {})

def detalle_ejemplo(request):
    return render(request, 'blog/ejemplo.html', {})