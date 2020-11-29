from django.urls import path, include
# this import things from settings.py file
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    # <int:blog_id>/ means anything in url, it shows that blog post
]
