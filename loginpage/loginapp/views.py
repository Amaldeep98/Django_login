from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Hardcoded username and password
VALID_USERNAME = 'amal'
VALID_PASSWORD = 'admin'

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            # Set session key
            request.session['username'] = username
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    # If already logged in, redirect to home
    if request.session.get('username'):
        return redirect('home')

    return render(request, 'login.html')


def home_view(request):
    if not request.session.get('username'):
        return redirect('login')
    
    return render(request, 'home.html')


def logout_view(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return redirect('login')
