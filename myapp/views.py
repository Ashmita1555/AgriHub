from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Business, Farmer, CommunityPost
from django.contrib.auth.decorators import login_required

# Home Page View
def home(request):
    return render(request, 'home.html')

# Register User View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# Logout View
def user_logout(request):
    logout(request)
    return redirect('login')

# User Profile Page
# @login_required
def profile(request):
    return render(request, 'profile.html')

# AgroMart View (Display Businesses)
def agro_mart(request):
    businesses = Business.objects.all()
    return render(request, 'agro_mart.html', {'businesses': businesses})

# Create Business Post View
@login_required
def create_business(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        # Add more fields as needed
        business = Business.objects.create(user=request.user, name=name, description=description)
        return redirect('business_detail', business_id=business.id)
    return render(request, 'create_business.html')

# Create Farmer Post View
@login_required
def create_farmer(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        quantity = request.POST['quantity']
        contact_number = request.POST['contact_number']
        farmer = Farmer.objects.create(user=request.user, product_name=product_name, quantity=quantity, contact_number=contact_number)
        return redirect('farmer_detail', farmer_id=farmer.id)
    return render(request, 'agromart/create_farmer.html')

# Community Page View
def community(request):
    posts = CommunityPost.objects.all()
    return render(request, 'community.html', {'posts': posts})

# Create Community Post View
@login_required
def create_community_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        community_post = CommunityPost.objects.create(user=request.user, title=title, content=content)
        return redirect('community')
    return render(request, 'create_community_post.html')

def test_page(request):
    return render(request, 'test.html')