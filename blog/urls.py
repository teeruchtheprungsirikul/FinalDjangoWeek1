from django.urls import path
from .views import (
    post_detail, say_hello, home
)

urlpatterns = [
    #path('url-name', function)
    path('hello', say_hello),
    path('', home, name="home"),
    path('blog/<int:pk>', post_detail)
]