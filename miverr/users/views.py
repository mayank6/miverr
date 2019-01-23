from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect,get_object_or_404,render
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from miverrapp.models import Gig

User=get_user_model()

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def logout_view(request):
    logout(request)
    return redirect('/')

def profile(request,username):
    if request.method=="POST":
        profile=User.objects.get(username=request.user.username)
        print(request.POST)
        try:
            profile.about=request.POST['about']
        except:
            pass
        try:
            profile.slogan=request.POST['slogan']
        except:
            pass
        profile.save()
    else:
        profile=get_object_or_404(User,username=username)
    gigs=Gig.objects.filter(user__username=profile.username)
    return render(request,"profile.html",{"profile":profile,"objects":gigs})
