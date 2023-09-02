# this will be the urls for the website 
# from django.contrib import admin these things are not required here at all
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeOne, name="home" ),
    path('register/',views.register_user, name="register" ),
    # path('reg/', views.reg1, name='reggo'), this was just for the purpose of testing the page

    # path('',views.login_user, name="login" ),
    path('logout/',views.logout_user, name="logout" ),
    path('records/<int:pk>',views.customer_info, name="records" ),
    path('delete_record/<int:pk>',views.delete_record, name="delete_record" ),
    path('add_record/',views.add_record, name="add_record" ),
    path('update_record/<int:pk>',views.update_record, name="update_record" ),






    # this naming convention is utilized for cases in the template where we need to link to the preferred template
    # path("",include('website.urls'))
]
