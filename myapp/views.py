from django.shortcuts import render,HttpResponse,redirect
from django.contrib import auth

from .models import Product,Profile
from django.contrib.auth.models import User

from .forms import CreateUserForm,LoginForm,UpdateUserForm,UpdateProfileForm

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.

def home(request):


	return render(request,'index.html')


def register(request):

	form = CreateUserForm()

	if request.method == 'POST':

		form=CreateUserForm(request.POST)

		if form.is_valid():

			current_user=form.save(commit=False)

			form.save()

			profile = Profile.objects.create(user=current_user)
			

			messages.success(request,"User regisration was successfull!")

			return redirect('my_login')
		
	context={'form': form}


	return render(request,'register.html', context=context)


def my_login(request):

	form = LoginForm
	
	if request.method == 'POST':

		form = LoginForm(request, data=request.POST)
		if form.is_valid():

			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request,username=username,password=password)

			if user is not None:

				auth.login(request,user)
				return redirect('dashboard')
			
	context = {'form': form}

	return render(request,'my_login.html',context=context)



def logout(request):
	auth.logout(request)

	return redirect("")




@login_required(login_url='my_login')
def dashboard(request):

	Products=Product.objects.all()

	context = {'Products': Products}



	return render (request,'dashboard.html',context=context)




@login_required(login_url='my_login')
def profile(request):


	profile = Profile.objects.get(user=request.user)

	user_form = UpdateUserForm(instance=request.user)

	form_2 =UpdateProfileForm(instance=profile)





	if request.method == 'POST':

		
	 
		user_form=UpdateUserForm(request.POST,instance=request.user)

		form_2 = UpdateProfileForm(request.POST, request.FILES,instance=profile)
		
		if user_form.is_valid():
			
			user_form.save()

			return redirect('dashboard')
		
		if form_2.is_valid():

			form_2.save()

			return redirect('dashboard')
		

	user_form = UpdateUserForm(instance=request.user)

	profile_pic= Profile.objects.get(user=request.user)


	context={'user_form':user_form, 'form_2':form_2,'profile':profile_pic}

	return render(request,'profile.html',context=context) 



@login_required(login_url='my_login')
def delete_profile(request):

	if request.method=='POST':

		deleteUser = User.objects.get(username=request.user)

		deleteUser.delete()

		return redirect("")
	

	return render(request,'delete.html')


# @login_required(login_url='my_login')
# def profile(request):
	
# 	profile_pic= Profile.objects.get(user=request.user)

# 	context ={'profile':profile_pic}


# 	return render(request,'profile.html',context=context)	