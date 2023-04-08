from django.views.generic import ListView
from .models import *
from django.shortcuts import render
# Create your views here.

class ImageListView(ListView):
    model = Image
    template_name = 'images/all_images.html'

def list(request):
    cat = Category.objects.all()
    context = {
        'list':cat,
    }
    return render(request, 'images/list.html', context)
