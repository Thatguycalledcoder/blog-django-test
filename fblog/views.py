from django.shortcuts import render, get_object_or_404

from blog.models import Post


def blog_list_view(request):
    posts = Post.objects.all()

    context = {"post_list": posts}

    return render(request, "home.html", context)


def blog_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post}
    return render(request, "post_detail.html", context)
