from django.shortcuts import render
from .models import Gig
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import GigForm

def home(request):
    gig=Gig.objects.filter(status=True)
    return render(request,'home.html',{"objects":gig})

def gig_detail(request,id):
    gig=get_object_or_404(Gig,id=id)
    return render(request,'gig_detail.html',{"gig":gig})

@login_required(login_url="/users/login/")
def create_gig(request):
    if request.method=="POST":
        gig_form=GigForm(request.POST,request.FILES)
        print(gig_form.is_valid())
        print(gig_form.errors())
    else:
        gig_form=GigForm()
    return render(request,'create_gig.html',{"form":gig_form})

@login_required(login_url="/users/login/")
def my_gigs(request):
    return render(request,'my_gigs.html',{})
