from django.urls import path,re_path
from . import views
from users.views import profile
app_name="miverrapp"

urlpatterns = [
    path("checkout/",views.create_purchase,name='checkout'),
    path("",views.home,name="home"),
    path("create-gig/",views.create_gig,name="create_gig"),
    path("mygig/",views.my_gigs,name="my_gigs"),
    re_path(r'^gigs/(?P<id>[\d-]+)/$',views.gig_detail,name="gig_detail"),
    re_path(r'^gigs/(?P<id>[\d-]+)/edit/$',views.edit_gig,name="gig_edit"),
    path("<username>/",profile,name="profile"),
    path("gigs/myselling/",views.my_selling,name="my_selling"),
    path("gigs/mybuying/",views.my_buying,name="my_buying"),
    re_path(r'^category/(?P<slug>[\w-]+)/$',views.category,name="category"),
]
