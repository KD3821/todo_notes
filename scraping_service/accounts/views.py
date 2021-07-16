from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from .forms import UserLoginForm, UserRegistrationForm, UserUpdateForm


User = get_user_model()

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        return render(request, 'accounts/register_done.html', {'new_user': new_user})
    return render(request, 'accounts/register.html', {'form': form})


def update_view(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = UserUpdateForm(request.POST)
            if form.is_valid():
                user.city = form.cleaned_data['city']
                user.language = form.cleaned_data['language']
                user.send_email = form.cleaned_data['send_email']
                user.save()
                return render(request, 'accounts/update_done.html', {'user': user})
            return render(request, 'accounts/update.html', {'form': form})
        else:
            form = UserUpdateForm(initial={'city': user.city, 'language': user.language, 'send_email': user.send_email})
            return render(request, 'accounts/update_done.html', {'user': user})
    else:
        return redirect('accounts:login')


def delete_view(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            qs = User.objects.get(pk=user.pk)
            qs.delete()
        return redirect('home')






# --- сам написал вьюху до просмотра урока ---
# def reg_view(request):
#     form = UserRegistrationForm(request.POST or None)
#     if form.is_valid():
#         data = form.cleaned_data
#         email = data.get('email')
#         password = data.get('password2')
#         user = User(email=email, password=password)
#         user.is_active = True
#         user.timestamp = DateTimeField(auto_now_add=True)
#         user.save()
#         return redirect('home')
#     return render(request, 'accounts/register.html', {'form': form})