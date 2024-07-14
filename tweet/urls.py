from django.urls import path

from . import views




urlpatterns=[
    path("",views.index,name='index'),
    path("tweet_create/",views.tweet_create,name="tweet_create"),
    path("tweet_list",views.tweet_list,name="tweet_list"),
    path('signup/',views.signup,name="signup"),
    path('login_user/',views.login_user,name="login_user"),
    path('tweet_delete/<int:tweet_id>/',views.tweet_delete,name='delete_tweet'),
    path('tweet_edit/<int:tweet_id>/',views.tweet_edit,name='tweet_edit'),
    path('logout',views.logout_user,name="logout_user"),
    path('about/',views.about,name="about"),
    path('contactus/',views.contactus,name="contactus"),
    path('search/',views.search,name="search"),


]