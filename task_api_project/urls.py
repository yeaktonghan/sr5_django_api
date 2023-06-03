from django.contrib import admin
from django.urls import path
from .views import index, detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/task', index),
    path('api/task/<int:id>/', detail)
]
