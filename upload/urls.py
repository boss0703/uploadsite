from django.urls import path

from upload.views import index

app_name = 'upload'
urlpatterns = [
    path('', index, name='index'),
]
