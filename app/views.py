from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm
from .models import Message
from .chatgpt import chatgpt_answer
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('chatbot')

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('chatbot')

    context = {'signupform': form}

    return render(request, 'signup.html', context=context)


def login(request):
    if request.user.is_authenticated:
        return redirect('chatbot')
    
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect('chatbot')

    context = {'loginform': form}

    return render(request, 'login.html', context=context)


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('home')


@login_required(login_url="/login")
def chatbot(request):
    if request.method == 'POST':
        if "chat-input" in request.POST:
            user = request.user
            messages = list(Message.objects.filter(user=user).order_by('timestamp'))
            question = request.POST.get('chat-input').strip()

            if question:
                answer = chatgpt_answer(messages, question)
                Message.objects.create(user=user, question=question, answer=answer)
        
        elif "delete-message" in request.POST:
            message_id = request.POST.get("delete-message")
            Message.objects.filter(id=message_id).delete()

        return redirect('chatbot')
    else:
        messages = list(Message.objects.filter(user=request.user).order_by('timestamp'))
        context = {'messages': messages}

    return render(request, 'chatbot.html', context=context)