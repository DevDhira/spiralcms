
from django.shortcuts import render,redirect
from blog.models import BlogPost
from .models import AuthorProfile
import dashboard.models as mod
from .forms import AuthorProfileForm
from django.db.models import Sum
from django.core.paginator import Paginator

# Create your views here.
def dashboard(request):
    posts = BlogPost.objects.filter(author_id = request.user.id)
    total_views = posts.aggregate(Sum('post_views'))['post_views__sum']
    paginator = Paginator(posts,6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request,'dashboard/dashboard.html',{'posts':posts,'value':total_views})

def profile(request):
    try :
        profile = AuthorProfile.objects.get(pk=request.user.id)
        return render(request,'dashboard/profile.html',{'profile':profile})
    except  Exception:
        return redirect('createprofile')

def createprofile(request):
    countries = str(mod.country_choices)
    if request.method == "POST":
        username = request.user
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        location = request.POST.get('location')
        current_role = request.POST.get('current_role')
        about = request.POST.get('about')
        AuthorProfile.objects.create(username=username,firstname=firstname,lastname=lastname,location=location,current_role=current_role,about=about)
        return redirect('profile')
    return render(request,'dashboard/create-profile.html',{'countries' : countries})

def editprofile(request):
    profile = AuthorProfile.objects.get(pk=request.user.id)
    form = AuthorProfileForm(request.POST or None , instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request,'dashboard/edit-profile.html',{'form':form})

