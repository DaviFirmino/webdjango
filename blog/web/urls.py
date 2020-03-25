from django.urls import path, include
from .views import hello_blog
from .views import work_detail, save_form



urlpatterns = [
    path('', hello_blog, name= 'home_blog'),
    path('work/<int:id>/', work_detail, name= 'work_detail'),
    path('save-form/', save_form, name='save_form')
]