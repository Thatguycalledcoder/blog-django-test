from django.urls import path
from .views import blog_list_view, blog_detail_view


urlpatterns = [
    path("post/<int:pk>/", blog_detail_view, name="fpost_detail"),
    path("", blog_list_view, name="fhome"),
]
