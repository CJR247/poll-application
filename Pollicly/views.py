from django.shortcuts import render,redirect
from .models import Question, Choice
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def UserLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'You are logged in')
            return redirect('index')
    return render(request,'Pollicly/login.html',{})

def UserLogout(request):
    logout(request)
    messages.success(request,"You're logged out!")
    return redirect('index')



def index(request):
    questions = Question.objects.all()
    return render(request, 'Pollicly/index.html', {'questions': questions})

def vote(request,pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    if request.method == 'POST':
        inputvalue = request.POST['choice']
        selection_option = options.get(id=inputvalue)
        selection_option.vote += 5
        selection_option.save()

    return render(request, 'Pollicly/vote.html', {'question':question, 'options': options })

def result(request, pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    if request.method == 'POST':
        inputvalue = request.POST['choice']
        selection_option = options.get(id=inputvalue)
        selection_option.vote += 5
        selection_option.save()
    return render(request, 'Pollicly/result.html', {'question': question, 'options': options})