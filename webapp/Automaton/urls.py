from django.urls import path
from Automaton import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index , name='index'),
    path('info\ ',views.info,name='info'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout_user'),
    path('profile',views.profile,name='profile'),
    path('forgot',views.forgot,name='forgot'),
    path('otp_verify',views.otp_verify,name='otp_verify'),
    path('book\ ',views.book,name='book'),
    path('book',views.book,name='book'),
    path('services',views.services,name='services'),
    path('otp_verify2',views.otp_verify2,name='otp_verify2')
]