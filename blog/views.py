from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import Post ,BlogComment
from django.contrib import messages
from blog.templatetags import extras

def index(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request,'blog/index.html',context)

def latestpost(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request,'blog/posts.html',context)

def blogpost(request,slug):
    if len(slug)>=1:
       try:
           Post.objects.get(slug=slug)
       except:
           return redirect('/blog/posts')
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post,parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request,'blog/blogpost.html',context)

def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno = postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno =="":
           Comment = BlogComment(comment = comment,user=user,post=post)
           Comment.save()
           messages.success(request," Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno= parentSno)
            Comment = BlogComment(comment = comment, user=user, post=post, parent=parent)
            Comment.save()
            messages.success(request, "Your reply has been posted successfully")
    return redirect(f'/blog/{post.slug}')
