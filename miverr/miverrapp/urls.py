from django.urls import path,re_path
from . import views

app_name="miverrapp"

urlpatterns = [
    path("",views.home,name="home"),
    path("create-gig/",views.create_gig,name="create_gig"),
    path("mygig/",views.my_gigs,name="my_gigs"),
    re_path(r'^gigs/(?P<id>[\d-]+)/$',views.gig_detail,name="gig_detail"),
]
