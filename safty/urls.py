from django.contrib import admin
from django.urls import path,include
from safty import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about", views.about, name='about'),
    path("child", views.child, name='child'),
    path("depression", views.depression, name='depression'),
    path("rape", views.rape, name='rape'),
    path("act", views.act, name='act'),
    path("rules", views.rules, name='rules'),
    path("login", views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logout'),
    path("signup", views.handleSignUp, name='signup'),
    path("cont", views.cont, name='cont'),
    path("share", views.share, name='share'),
    path("pc", views.pc, name='pc'),
    path("rape1", views.rape1, name='rape1'),
    path("back", views.back, name='back'),
    path("backlogin", views.backlogin, name='backlogin'),
    path("rule", views.rule, name='rule'),
    path("stalking", views.stalking, name='stalking'),
    path("sexual", views.sexual, name='sexual'),
    path("domesticvoilence", views.domesticvoilence, name='domesticvoilence'),
]
