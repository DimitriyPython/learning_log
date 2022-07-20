from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Registring a new user"""
    if request.method != 'POST':
        # Enter an empty form of registration
        form = UserCreationForm()
    else:
        # Processing of full form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log in and redirect on homepage
            login(request, new_user)
            return redirect('learning_logs:index')

    # Output empty or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
