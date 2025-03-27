from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Chat
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('full_name')
        mo_number = request.POST.get('mobile_number')
        password = request.POST.get('password')
        username = f"user_{mo_number}"

        try:
            user = User.objects.get(username=username)
            user_auth = authenticate(request, username=username, password=password)
            if user_auth is not None:
                login(request, user_auth)
                return redirect('/')
            else:
                messages.error(request, "Wrong password")
                return redirect('signup')
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, password=password, first_name=name)
            login(request, user)
            return redirect('/')

    return render(request, 'myapp/signup.html')

@login_required(login_url='/signup')
def chat_home(request):
    query = request.GET.get('query')
    users = []
    if query: 
        users = User.objects.filter(username__icontains=query).distinct()
    return render(request, 'myapp/chat.html', {'users': users})

@login_required(login_url='/signup')
def start_chat(request, username):
    user = User.objects.get(username=username)
    current_user = request.user.username

    # Chat fetch करो दोनों तरफ की (sender ya receiver koi bhi ho sakta hai)
    chats = Chat.objects.filter(
        (Q(sender=current_user) & Q(receiver=username)) |
        (Q(sender=username) & Q(receiver=current_user))
    ).order_by('timestamp')

    return render(request, 'myapp/start_chat.html', {'user': user, 'chats': chats})
@login_required(login_url='/signup')
def send_chat(request):
    if request.method == 'POST':
        sender = request.user.username
        receiver = request.POST.get('receiver')
        chat_msg = request.POST.get('chat')
        if receiver and chat_msg:
            Chat.objects.create(sender=sender, receiver=receiver, message=chat_msg)
            return redirect('start_chat', username=receiver)
    return redirect('chat_home')

@login_required(login_url='/signup')
def receive_chat(request, username):
    current_user = request.user.username
    chats = Chat.objects.filter(
        (Q(sender=current_user) & Q(receiver=username)) | (Q(sender=username) & Q(receiver=current_user))
    ).order_by('timestamp')
    return render(request, 'myapp/start_chat.html', {'chats': chats, 'receiver': username})