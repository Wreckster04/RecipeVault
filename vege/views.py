from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from vege.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
# Create your views here.
@login_required(login_url='/login')
def create(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('recipe_name')
        desc = data.get('recipe_desc')
        image = request.FILES.get('recipe_image')
        if not name or not desc or not image:
            return 
        Recipe.objects.create(
            recipe_name = name,
            recipe_desc = desc,
            recipe_image = image
        )
        return redirect('/recipes')
            
            
    return render(request, "recipes.html")
@login_required(login_url='/login')
def read(request):
    data = Recipe.objects.filter(user = request.user)
    context = {'fulldata':data}
    return render(request,"display.html",context)
@login_required(login_url='/login')
def update(request,id):
    querySet = Recipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        name = data.get('recipe_name')
        desc = data.get('recipe_desc')
        image = request.FILES.get('recipe_image')
        querySet.recipe_name = name
        querySet.recipe_desc = desc
        if image:
            querySet.recipe_image = image
        querySet.save()
        return redirect('/recipes')
    return render(request, "update.html", {'recipe':querySet})
@login_required(login_url='/login')
def delete(request,id):
    querySet = Recipe.objects.get(id=id)
    querySet.delete()
    return redirect('/read')
@login_required(login_url='/login')
def search(request):
    if request.GET.get('search'):
        search = request.GET.get('search')
        data = Recipe.objects.filter(recipe_name__icontains=search)
        if not data:
            return render(request, "display.html", {'message':"No results found"})
        else:
            context = {'fulldata':data}
            return render(request,"display.html",context)   
            context = {'fulldata':data}
            return render(request,"display.html",context)
    else:
        data = Recipe.objects.all()
        context = {'fulldata':data}
        return render(request,"display.html",context)
def signup(request):
    if request.method == "POST":
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        username = data['username']
        password = data['password']
        if not all([first_name,last_name,username,password]):
            messages.info(request, "Please fill all fields")
            return redirect('/signup')
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists")
            return redirect('/signup')
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )
        user.save()
        messages.info(request, "Account created successfully. Please login.")
        return redirect('/login')
    return render(request, "signup.html")
def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.info(request, "Please fill all fields")
            return redirect('/login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/recipes')  # Change to your dashboard route if needed
        else:
            messages.info(request, "Invalid username or password")
            return render(request, "signin.html")

    return render(request, "signin.html")
def logout_page(request):
    logout(request)
    return redirect('/login')