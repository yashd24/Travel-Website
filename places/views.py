from django.shortcuts import render, redirect
from .models import places
from .forms import MyForm, signup_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail


def home(request):
    ele = places.objects.all()
    return render(request, "places/home.html", {
        "ele": ele
    })


@login_required(login_url='login')
def add(request):
    form = MyForm()
    content = {'form': form}
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'places/add.html', content)


def delete(request, id):
    place = places.objects.get(id=id)
    if request.method == "POST":
        place.delete()
        print(place)
        return redirect('home')
    return render(request, "places/delete.html", {'obj': place})


def user_login(request):

    ele = places.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return render(request, 'places/admin_home.html', {'ele': ele})

            else:
                return render(request, 'places/loggedin.html', {'ele': ele})

        else:
            error_message = "Incorrect Credentials"
            messages.error(request, error_message)
            return render(request, 'places/login.html')

    return render(request, 'places/login.html')


def register(request):
    form = signup_form()
    if request.method == "POST":
        form = signup_form(request.POST)
        if form.is_valid():

            email = request.POST.get('email')
            print(type(email), email)

            send_mail(
                'Welcome To Travello',
                'Congratulations!! You Have Successfully Registered',
                'yash.test.noreply@gmail.com',
                [email],
                fail_silently=False,
            )
            form.save()

            return redirect('login')

    return render(request, 'places/signup.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')
