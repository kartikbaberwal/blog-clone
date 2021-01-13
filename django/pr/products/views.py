from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Posts,Comments
from .forms import post_creation,signup_form,login_form
from django.contrib.auth.models import User,auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
def home(request):
    posts=Posts.objects.all()
    context={
         'posts':posts
    }
    return render(request,"products/first.html",context)
def create_post(request):
     form=post_creation(request.POST or None)
     if form.is_valid():
          obj=form.save(commit=False) 
          obj.author=request.user; 
          obj.save() 
          form.save()
          return HttpResponse("blog added")
     form={'form':form}
     return render(request,"products/create.html",form)

def signup(request): 
     form=signup_form()
     if(request.method=='POST'):
          form=signup_form(request.POST)
          if(form.is_valid):
               username=request.POST['username']    
               email=request.POST['email']    
               password=request.POST['password']
               temp=User.objects.filter(username=username).exists()
               if(temp==0):
                    user=User.objects.create_user(username=username,email=email,password=password)    
                    user.save()
                    temp=auth.authenticate(username=username,password=password)
                    if(temp):
                        auth.login(request,temp)    
                        return redirect("/home/")    
     form={'form':form}
     return render(request,"products/signup.html",form)

def login(request): 
     form=login_form()
     if(request.method=='POST'):
          form=login_form(request.POST)
          if(form.is_valid):
               username=request.POST['username']      
               password=request.POST['password']
               temp=auth.authenticate(username=username,password=password)
               if(temp):
                    auth.login(request,temp)    
                    return redirect("/home/")   
     form={'form':form}
     return render(request,"products/signup.html",form)

def logout(request):
     auth.logout(request)
     return redirect("/home")

def detail_view(request,pk):
    obj=Posts.objects.filter(id=pk).first()
    comments=Comments.objects.filter(post=obj)
    context={
         'post':obj,
         'comments':comments
     }
    return render(request,"products/detail_view.html",context)

def delete_view(request,pk):
    posts=Posts.objects.filter(id=pk).first()
    posts.delete()
    return redirect("/home/")

def update_view(request,pk):
     post=Posts.objects.filter(id=pk).first()
     form=post_creation(instance=post)
     if request.method=="POST":
          form=post_creation(request.POST,instance=post)
          if form.is_valid:
              form.save()
              return redirect("/home/")
     context={'form':form}         
     return render(request,"products/create.html",context)   

def search(request):
     query=request.GET['query']
     posts=Posts.objects.filter(title__icontains=query)
     content=Posts.objects.filter(content__icontains=query)
     posts=posts.union(content)
     context={'posts':posts}
     return render(request,"products/first.html",context)

def comment(request):
     if request.method=="POST":
         content=request.POST['content']
         postid=request.POST['post']
         post=Posts.objects.get(id=postid)
         author=request.user
         comment=Comments(content=content,author=author,post=post)
         comment.save()
         return redirect(f"/blog/{post.id}")

def reply(request):
     if request.method=="POST":
         content=request.POST['content']
         postid=request.POST['post']
         commentid=request.POST['comment']
         post=Posts.objects.get(id=postid)
         comment=Comments.objects.get(id=commentid)
         author=request.user
         comment=Comments(content=content,author=author,post=post,parent=comment)
         comment.save()
         return redirect(f"/blog/{post.id}")

def reset_pass(request):
     if request.method == 'POST':
          form = PasswordChangeForm(request.user, request.POST)
          if form.is_valid():
               user = form.save()
               update_session_auth_hash(request, user)  # Important! otherwise user would have to login again
               return redirect('/home/')
     else:
          form = PasswordChangeForm(request.user)
     return render(request, 'products/change_password.html', {'form': form})          