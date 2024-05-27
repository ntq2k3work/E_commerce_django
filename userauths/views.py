from django.shortcuts import render,redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if(form.is_valid()): 
            user = form.save()
            username = form.cleaned_data["username"]
            messages.success(request,f"Tài khoản {username} đã được đăng ký thành công !")            
            # print("Đăng ký thành công !")
            user = authenticate(username = form.cleaned_data['email'], password = form.cleaned_data['password1'] )
            login(request,user)
            return redirect("core:index")
            
    else:
        print("Không thể đăng ký !")
    form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request,'userauths/register.html', context)


def login_view(request):
    # if request.method == "POST":
        
    return render(request,'userauths/login.html')