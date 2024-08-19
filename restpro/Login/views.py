from django.shortcuts import render,redirect

# Create your views here.
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('demo')
    else:
        form = CreationUserForm()
        context = {'form': form}
        if request.method == 'POST':
            form = CreationUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, user + 'Registered Successfully.')
            return redirect('login')
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('demo')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                redirect('demo')
            else:
                messages.info(request, 'Incorrect Username or Password ')
        context = {}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')