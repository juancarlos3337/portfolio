from django.shortcuts import render,get_object_or_404
from .models import Post
def render_posts(request):
    posts= Post.objects.all()
    return render(request,'post.html',{'posts':posts})

def post_detalle(request,post_id):
    post=get_object_or_404(Post, pk=post_id)
    return render(request,'post_detalles.html',{"post":post})