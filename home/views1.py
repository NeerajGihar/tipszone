from django.shortcuts import render, HttpResponse,redirect
from home.models import contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout

def home(request):
    return HttpResponse("Home")

def Contact(request):
    if request.method == "POST":
        fname = request.POST['fname']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(fname)<2 or len(email)<5 or len(phone)<10 or len(content)<10:
            messages.error(request,"Please fill the form correctly")
        else:
            Contact = contact(name=fname, email=email, phone=phone, content=content)
            Contact.save()
            messages.success(request,"Your message has been successfully sent")
    
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')

def search(request):
    query = request.GET['query']
    if len(query)>80:
        allPosts = Post.objects.none()
    else:
        allPostTitle = Post.objects.filter(title__icontains=query)
        allPostauthor = Post.objects.filter(author__icontains=query)
        allPostcontent = Post.objects.filter(content__icontains=query)
        allPosts = allPostauthor.union(allPostcontent,allPostTitle)
    if allPosts.count()==0:
        messages.warning(request,"No search results found. Please refine your query.") 
    param = {'allPosts':allPosts,'query':query}
    return render(request,'home/search.html',param)

def SignUp(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        fname =  request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        usercheck = username
        if len(username)>10:
            messages.error(request,' Your user name must be under 10 characters')
            return redirect('/blog')
        if not username.isalnum():
            messages.error(request,' User name should only contain letters and numbers')
            return redirect('/blog')

        if (pass1 != pass2):
            messages.error(request,' Passwords do not match')
            return redirect('/blog')
        
        try:
            user= User.objects.get(username=usercheck)
            messages.error(request,' User name already used try another!')
            return redirect('/blog')
        except User.DoesNotExist:
            myuser = User.objects.create_user(username,email,pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request,'Your TipZone account has been successfully created')
            return redirect('/blog')
    else:
        return HttpResponse('404 Error not found')

def LogIn(request):
    if request.method == "POST":
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]
        user = authenticate(username = loginusername, password = loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request," Successfully Logged In")
            return redirect('blog/')
        else:
            messages.error(request," Invalid credentials! Please try again")
            return redirect('blog/')
    else:
        return HttpResponse("404 Error Page Not Found")


    

def LogOut(request):
    logout(request)
    messages.success(request,' Successfully logged out')
    return redirect("blog/")