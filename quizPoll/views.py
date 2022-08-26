from turtle import title
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Questions

# Create your views here.

def registration(request):
    if request.method == "POST":
        username=request.POST["username"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        password=request.POST["pass1"]
        confirm_password=request.POST["pass2"]
        if password == confirm_password:
            user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            messages.info(request,"Registration successfull")
            return redirect("login_page")
        else:
            messages.info(request,"Password is not matching")
            return redirect("registration")
    return render(request, "registration.html")


def login_page(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["pass1"]
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            messages.info(request,"Username and password is not matching....")
            return redirect("login_page")
    return render(request, "login.html")


def homepage(request):
    polls=Questions.objects.all()
    return render(request, "homepage.html", {'polls':polls})

def add_poles(request):
    if request.method == "POST":
        questions=request.POST['question']
        option_one=request.POST['opt1']
        option_two=request.POST['opt2']
        option_three=request.POST['opt3']
        option_foure=request.POST['opt4']
        poll=Questions.objects.create(questions=questions, option_one=option_one, option_two=option_two,    option_three=option_three, option_foure=option_foure)
        poll.save()
        return redirect('homepage')
    return render(request, "add-poles.html")



def vote(request, id):
    poll = Questions.objects.get(id=id)
    if request.method == "POST":
        print(request.POST["poll"])
        selected_option = request.POST["poll"]
        if selected_option == "option1":
            poll.option_one_count += 1
        elif selected_option == "option2":
            poll.option_two_count += 1
        elif selected_option == "option3":
            poll.option_three_count += 1
        elif selected_option == "option4":
            poll.option_foure_count += 1
        else:
            return HttpResponse(400, "Invailid form")
        poll.save()
        return redirect('result',poll.id)
    return render(request, 'vote.html',{'poll':poll})

def result(request, id):
    poll=Questions.objects.get(id=id)
    return render(request, 'result.html', {'poll':poll})

def logoutView(request):
    logout(request)
    print("log outtttttttttttttttttttttttttttt")
    return redirect('login_page')

def my_profile(request):
    if request.user.is_authenticated:
        return render(request, 'my_profile.html')
    else:
        return redirect('login_page')
    
    
