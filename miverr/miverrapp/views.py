from django.shortcuts import render,redirect
from .models import Gig
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import GigForm
from django.http import Http404

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
        if gig_form.is_valid():
            gig=gig_form.save(commit=False)
            gig.user=request.user
            gig.save()
            return redirect('miverrapp:my_gigs')
    else:
        gig_form=GigForm()
    return render(request,'create_gig.html',{"form":gig_form})


@login_required(login_url="/users/login/")
def edit_gig(request,id):
    gig=get_object_or_404(Gig,id=id)
    if request.user ==gig.user:
        if request.method=="POST":
            gig_form=GigForm(request.POST,request.FILES,instance=gig)
            if gig_form.is_valid():
                gig=gig_form.save(commit=False)
                gig.save()
                return redirect('miverrapp:my_gigs')
        else:
            gig_form=GigForm(instance=gig)
    else:
        raise Http404
    return render(request,'edit_gig.html',{"form":gig_form})



@login_required(login_url="/users/login/")
def my_gigs(request):
    gigs=Gig.objects.filter(user=request.user)
    return render(request,'my_gigs.html',{"gigs":gigs})
