from django.shortcuts import render,redirect
from .models import Gig,purchase,review
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import GigForm
from django.http import Http404
import braintree

braintree.Configuration.configure(braintree.Environment.Sandbox,merchant_id="jvfr2jhb59fv74s9",
public_key="gr7skyy72nmbkp5j",private_key="6eddf2ae3bb880fa59d4ff9a8e5c96e9")


def home(request):
    gig=Gig.objects.filter(status=True)
    return render(request,'home.html',{"objects":gig})

def gig_detail(request,id):
    if request.method=="POST" and "content" in request.POST:
        print("working")
        review.objects.create(content=request.POST['content'],user=request.user,gig_id=id)
        print("working")
    gig=get_object_or_404(Gig,id=id)
    reviews=review.objects.filter(gig=gig)
    if request.user.is_anonymous or review.objects.filter(gig=gig,user=request.user).count()>0:
        sr=False
    else:
        sr=purchase.objects.filter(gig=gig,buyer=request.user).count()>0
    client_token=braintree.ClientToken.generate()
    return render(request,'gig_detail.html',{"sr":sr,"reviews":reviews,"gig":gig,"client_token":client_token})

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


@login_required(login_url="/users/login/")
def create_purchase(request):
    if request.method=="POST":
        gig=get_object_or_404(Gig,id=request.POST['gig_id'])
        nonce=request.POST["payment_method_nonce"]
        result=braintree.Transaction.sale({
            "amount":gig.price,
            "payment_method_nonce":nonce
        })
        if result.is_success:
            purchase.objects.create(gig=gig,buyer=request.user)
    return redirect("/")

@login_required(login_url="/users/login/")
def my_selling(request):
    p=purchase.objects.filter(gig__user=request.user)
    return render(request,'my_selling.html',{'purchases':p})

@login_required(login_url="/users/login/")
def my_buying(request):
    p=purchase.objects.filter(buyer=request.user)
    return render(request,'my_buying.html',{'purchases':p})

def category(request,slug):
    print(slug)
    c={
    "graphic-designing":"GD",
    "digital-marketing":"DM",
    "content-writing":"CW",
    "game-animation":"GM",
    "music-video":"MV",
    }
    try:
        gigs=Gig.objects.filter(category=c[slug])
        return render(request,"home.html",{"objects":gigs})
    except:
        return redirect('home')
