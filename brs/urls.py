from django.urls import path
from .import views
urlpatterns =[
    path('',views.home,name='home'),
    path('signup',views.signup ,name='signup'),
    path('logins',views.logins ,name='logins'),
    path('booking',views.booking ,name='booking'),
    path('logout',views.logouts,name='logout'),
    path('contact',views.contact ,name='contact')   
]