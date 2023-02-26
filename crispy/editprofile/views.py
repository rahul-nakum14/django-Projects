from django.shortcuts import render,redirect
from main.forms import UserRegisterForm,UserUpdadeform,Profileform
from django.contrib.auth.models import User


def edit_profile(request, user_id):
    post = User.objects.get(id=user_id)
    if request.method == "POST":
        form = UserRegisterForm(request.POST, instance=post) 
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm(instance=post)
    return render(request, 'main/edit_profile.html', {'form': form})


def profile(request):
    if request.method == "POST":
        u_form = UserUpdadeform(request.POST,instance=request.user)
        p_form = Profileform(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
    else:
        u_form = UserUpdadeform(instance=request.user)
        p_form = Profileform(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form,
    }

    return render(request, 'main/edit_profile.html', context)
# def edit_profile1(request):
#     user= request.user.user_profile
#     form = user_profile_form(instance=user)
#     return render(request, 'main/edit_profile.html', {'form': form})




