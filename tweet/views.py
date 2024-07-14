from django.shortcuts import render,redirect
from .models import Tweet
from .forms import TweetForm,SignUpForm,ContactUsForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q

# Create your views here.


def search(request):
    if request.method=="POST":
        searched=request.POST["searched"]
        tweets=Tweet.objects.filter(Q(text__icontains=searched))
        if  tweets:
            print("if working")
            print(tweets)
            return render(request,"search.html",{"tweets":tweets})
        else:
            print("else working")

            print(tweets)
            messages.success(request,"please search somethong else!")
            return render(request,"search.html")
    else:
        messages.success(request,"please search somethong else!")
        return redirect('index')
        
   

def contactus(request):
    if request.method=="POST":
        form=ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Hey Your Query is saveed. We Will Contact you Soon!")
            return redirect('index')

    form=ContactUsForm()
    return render(request,"contactus.html",{"form":form})

def about(request):
    return render(request,"aboutus.html")

def index(request):
    tweets=Tweet.objects.all()
    return render(request,'index.html',{"tweets":tweets})




def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request,"tweet_list.html",{"tweets":tweets})



def tweet_create(request):
        if request.user.is_authenticated:
    
            if request.method=="POST":

                form=TweetForm(request.POST,request.FILES)
                if form.is_valid():
                    tweet=form.save(commit=False)
                    tweet.user=request.user
                    tweet.save()
                    return redirect('tweet_list')

            else:
                form=TweetForm()
            return render(request,"tweet_form.html",{"form":form})
        else:
            messages.success(request,"plese ensure are a loged in user!")
            return redirect("login_user")
        
        



def tweet_edit(request,tweet_id):
    tweet=get_object_or_404(Tweet,user=request.user,pk=tweet_id)
    form=TweetForm(instance=tweet)
    print(tweet)

    if request.method=="POST":
        form=TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            messages.success(request,"hey your tweet is updated !")
           
            return redirect('tweet_list')


        
    
    return render(request,"update.html",{"form":form})



def tweet_delete(request,tweet_id):
    try:
        tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    

        tweet.delete()
        messages.success(request,"tweet delete succesfully !")
        return redirect("tweet_list")
        #return render('tweet_list')
    except :
        messages.success(request,"only real user can delete their tweet!")
        return redirect('index')



def signup(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"user registed successfully!")
    return render(request,"signup.html",{"form":form})




def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)

            messages.success(request,f"hey {request.user.first_name} you login successfully!")
            return redirect('index')
        else:
            messages.success(request,"login failed ples try again!")
    return render(request,"login.html")

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logout!")
    return redirect('login_user')