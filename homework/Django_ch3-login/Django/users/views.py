from django.shortcuts import render

def profile(req):
    return render(req, 'users/profile.html')