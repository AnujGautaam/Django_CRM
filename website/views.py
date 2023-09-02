from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout 
from django.contrib import messages
from .forms import signUpForm, AddRecordForm
from .models import Record

# Create your views here.
# it falls in one of the steps for the creation and execution of a page in django which is to 
# this is where the functions will be defined 

def homeOne(request):
    # this is for fulfilling the conditions applied in the html pages 
    
    records = Record.objects.all()
    
    if (request.method=="POST"):
        username = request.POST['username']
        password = request.POST['password']
        # next is the task of autheticating the users
        user = authenticate(request, username = username, password=password)
        # print(username,password)
        if(user is not None):
            login(request, user)
            messages.success(request,"congrats, you have successfully loggedin to the system!!!")
            return redirect('home')
        else:
            messages.success(request,"sorry the login failed ")
            return redirect('home')

    else:
        return  render(request, "home.html", {'records':records})



# next are the tasks of adding in the login and logout for the website
# 
def login_user(request):
    pass

def logout_user(request):
    # this is for logging out the users
    logout(request)
    messages.success(request,"you have successfully logged out of the account") 
    return redirect('home')

# one of the goals of this session is to test if i am able to write a suitable code for loggin in and out of the user 
# lets see 

# next is the registration of the user and this is going to be done in a manner that will be useful for validating everything and all the things 
def register_user(request):
    # check if the method used during the submission of the form is post or not 
    if request.method=='POST':
        form = signUpForm(request.POST)
        # if the form is valid saving it 
        if form.is_valid():
                form.save()
                # next is the task of authenticating and allowing the user to login 
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username = username, password= password) 
                #this will validate that the user is logged in thus he/she should be allowed to login now
                login(request, user)
                messages.success(request,"you have successfully logged in. congrautations!!! ")
                return redirect('home')
        # the upper one is the condition where the user has filled the form and has pushed the signup button,
        #the else statemetn to this case is when the user is just at the page and has not filled out the details and submitted the form yet and this should be treated as such 
    else:
            form = signUpForm()
            return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})


# this will be for testing out if the register page works or not and this is just for that purpose 
# def reg1(request):
#     return render(request, 'register.html') 
# mission successful in this one 

# the code has finally worked and the solution to the issue was that the else statement was not where it should have beena dn this has been thoroughly resolved. 


def customer_info(request, pk):
     if request.user.is_authenticated:
          customer_records= Record.objects.get(id=pk)
        #   if the user exists and there is a record of the user, the look into the records for that user
          return render(request, 'records.html',{'customer_records':customer_records})
     else:
        messages.success(request,"sorry you have to be logged in to continue this")
        return redirect('home') 

# the next task is to include the url so clicking it would give more information on the user 


def delete_record(request,pk):
     if request.user.is_authenticated:
          delete_it = Record.objects.get(id=pk)
          delete_it.delete()
          messages.success(request,"the record has been taken off the record successfully")
          return redirect('home')
     else:
          messages.success(request,"you have to be logged in to perform this action")
          return redirect('home')
     
def add_record(request):
     form = AddRecordForm(request.POST or None)
     if request.user.is_authenticated:
          if request.method == "POST":
               if form.is_valid():
                    add_record = form.save()
                    messages.success(request, "the record has been created")
                    return redirect('home')
         
          return render(request, 'add_record.html',{'form':form})
  
     else:
          messages.success(request, 'you have to be registered in order to create the registration of the users')
          return redirect('home')
          

                    
               
          
def update_record(request,pk):
        #first check whether the client has signed up or not
    if request.user.is_authenticated:
         current_record = Record.objects.get(id=pk)
         form = AddRecordForm(request.POST or None, instance=current_record)
         if form.is_valid():
              form.save()
              messages.success(request,"congratulations!!!, you have successfully updated the information on the client")
              return redirect('home')
         return render(request, 'update_record.html', {'form':form})
    else:
         messages.success(request, 'you have to be logged in to update the information on the client')
         return redirect('home')
    

# next is the task of updating the register form and ensuring that it will register all the details inside of the client's folder
# so he only stole 100 thousand dollars from this account and is comparitively its not much 