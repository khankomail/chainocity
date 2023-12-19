from django.shortcuts import render,HttpResponse,redirect
from django.contrib import auth

from .models import Product

from .forms import CreateUserForm,LoginForm

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):


	return render(request,'index.html')


def register(request):

	form = CreateUserForm()

	if request.method == 'POST':

		form=CreateUserForm(request.POST)

		if form.is_valid():

			form.save()

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








