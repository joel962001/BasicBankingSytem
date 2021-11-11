from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('tp',views.tp,name='tp'),
    path('history',views.history,name='history'),
    path('new',views.new,name='new'),
    path('transaction/<int:sr_no>/',views.transaction),
]
