from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Create your views here.

# Using built in django authentication create a login view
def user_login_view(request):
    if request.user.is_authenticated:
        return render(request, 'user/userhome.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('../user/userhome/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'home.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'home.html', {'form': form})


# Using built in Django authentication
def user_signup_view(request):
    if request.user.is_authenticated:
        return redirect('home/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home/')
        else:
            return render(request, 'user/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'user/signup.html', {'form': form})


def user_signout(request):
    logout(request)
    return redirect('/home/')


def user_home_view(request):
    context = {
        'test': 1
    }
    return render(request, 'user/userhome.html', context)
