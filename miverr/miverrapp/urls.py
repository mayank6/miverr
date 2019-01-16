from django.urls import path,re_path
from . import views

app_name="miverrapp"

urlpatterns = [
    path("",views.home,name="home"),
    re_path(r'^gigs/(?P<id>[\d-]+)/$',views.gig_detail,name="gig_detail"),
]
