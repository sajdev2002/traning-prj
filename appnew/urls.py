from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('tableview',views.tableview,name='tableview'),
    path('user_delete/<int:id>',views.user_delete,name='user_delete'),
    path('user_edit/<int:id>/',views.user_edit,name='user_edit'),
]