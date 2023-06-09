from django.urls import path
from django.views.generic import TemplateView
from .views import ImageListView
app_name = 'images'
from .import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="images/index.html")),
    path('wallpapers/', ImageListView.as_view(), name='images'),
    path('categories/',  views.list, name="list")
]
