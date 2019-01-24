from django.shortcuts import render,redirect
from .models import Gig
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
    gig=get_object_or_404(Gig,id=id)
    client_token=braintree.ClientToken.generate()
    return render(request,'gig_detail.html',{"gig":gig,"client_token":client_token})

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
            print("Buy Gig success")
        else:
            print("Buy Gig Failed")
    return redirect("/")
