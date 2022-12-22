
from blog.forms import AuthorSignupForm, BlogPostForm
from django.shortcuts import render,redirect
from .models import BlogPost
from slugify import slugify
from django.contrib import messages
from django.core.paginator import Paginator


#seperate functions
def listToString(s): 
    
    str1 = ""   
  
    for ele in s: 
        str1 += " "+ele  
    return str1 
        


# Create your views here.
def index(request):
    posts = BlogPost.objects.all().order_by('date').reverse()
    paginator = Paginator(posts,9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'blog/home.html',{'posts':posts})

def fullpost(request,slug):
    post = BlogPost.objects.get(urlslug=slug)
    post.post_views = post.post_views + 1 
    post.save()
    
    return render(request,'blog/fullpost.html',{'post':post})

def authorregister(request):
    form = AuthorSignupForm(request.POST or None)
    try:
        if form.is_valid():
            form.save()
            messages.success(request,"Registered Successfully")
            return redirect('login')   
    except Exception as e:
        messages.error(request,e)   
        return redirect('signup')     
    return render(request,'blog/authorsignup.html',{'form':form})


def createpost(request):
    form = BlogPost()
    print(request.user)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        excerpt= listToString(content.split()[:20]) +"..."
        image=request.POST.get('image')
        author= request.user
        category = request.POST.get('category')
        if request.POST.get('urlslug') == "":
            urlslug = slugify(title)
        else :
            urlslug = request.POST.get('urlslug')
        print(urlslug)
        BlogPost.objects.create(title=title,content=content,excerpt=excerpt,image=image,author=author,category=category,urlslug=urlslug)
        messages.success(request,"Post Created Successfully")
        return redirect('home')
    return render(request,'blog/createpost.html')

def editpost(request,urlslug):
    post = BlogPost.objects.filter(urlslug=urlslug).first()
    post_form = BlogPostForm(request.POST or None , instance=post)
    if post_form.is_valid():
        post_form.save()
        messages.success(request,"Post Updated")
        return redirect('dashboard')
    return render(request,'blog/editpost.html',{'post_form':post_form})







