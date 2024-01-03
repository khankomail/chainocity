from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from django.contrib import auth

from django.http import JsonResponse 

from .models import Product,Profile,Category,Code,Plan,Cart,CartItem,Order
from django.contrib.auth.models import User

from .forms import CreateUserForm,LoginForm,UpdateUserForm,UpdateProfileForm,CheckoutForm

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.

def home(request):


	return render(request,'index.html')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            current_user = form.save(commit=False)
            form.save()

            # Create user-related objects
            profile = Profile.objects.create(user=current_user)
            plan = Plan.objects.create(user=current_user)
            code = Code.objects.create(user=current_user)
            code.my = Code.generate_code()
            code.save()

            # Create a cart and associate it with the user
            cart = Cart.objects.create(user=current_user)

            messages.success(request, "User registration was successful!")

            return redirect('my_login')

    context = {'form': form}
    return render(request, 'register.html', context=context)


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

	Categorys=Category.objects.all()
	
	

	user_cart = Cart.objects.get(user=request.user)
	cart_items = user_cart.items.all()
	cart_items_count = cart_items.count()


	context = {'Products': Products, 
						'Categorys':Categorys,
						'cart_items': cart_items,
        		'cart_items_count': cart_items_count,}



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



@login_required(login_url='my_login')
def product(request,pk):
	product=Product.objects.get(id=pk)
	context={
		'product':product
	}
	return render(request,'product_detail.html',context=context)


@login_required(login_url='my_login')
def category(request,ct):

	ct=ct.replace('-',' ')

	try:
		category = Category.objects.get(name=ct)
		products = Product.objects.filter(category=category)

		context={'products': products, 'category':category}

		return render(request,'category.html' ,context=context)

	except:
		return redirect('dashboard')

	
@login_required(login_url='my_login')
def mylink(request):

	plan = Plan.objects.get(user=request.user)
	code = Code.objects.get(user=request.user)

	context={'plan':plan , 'code':code}



	return render(request,'mylink.html',context=context)



@login_required(login_url='my_login')
def plan(request):
    plan = Plan.objects.get(user=request.user)

    try:
        code = Code.objects.get(user=request.user)
    except Code.DoesNotExist:
        # Handle the case when the Code object doesn't exist for the user
        code = None

    if request.method == 'POST':
        # Get the updated value from the form data
        new_other_value = request.POST.get('other_value', None)

        if code is not None:
            # Update the 'other' field if the Code instance exists
            code.other = new_other_value
            code.save()

        return redirect('plan')

    context = {'plan': plan, 'code': code}
    return render(request, 'plan.html', context=context)



@login_required(login_url='my_login')
def earning(request):

	code = Code.objects.get(user=request.user)

	code_users = Code.objects.filter(other=code.my)


	context={'code':code,'code_users':code_users}

	return render (request,'earning.html',context=context)


@login_required(login_url='my_login')
def cart(request):
    # Assuming user's cart is already created during registration or login
			user_cart = Cart.objects.get(user=request.user)
			cart_items = user_cart.items.all()
			
			if request.method == 'POST':
				cart_item_id = int(request.POST.get('cart_item_id'))
				cart_item = CartItem.objects.get(id=cart_item_id)
				cart_item.delete()
				return redirect('cart')
			
			context={
				'cart_items': cart_items,
			}

			return render(request, 'cart.html', context=context)
		

		


@login_required(login_url='my_login')
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    print(f"DEBUG: cart_add view called for product ID {product_id}.")

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))

        # Create a CartItem instance
        cart_item = CartItem(product=product, quantity=quantity, user=request.user)
        cart_item.save()

        # Assuming user's cart is already created during registration or login
        user_cart = Cart.objects.get(user=request.user)
        user_cart.items.add(cart_item)

        # Add a success message
        messages.success(request, f"{product.p_title} added to your cart.")
        print(f"DEBUG: {product.p_title} added to cart.")

    # Redirect to the product detail page
    return redirect('dashboard')

	



@login_required(login_url='my_login')
def cart_delete(request):
	pass




@login_required(login_url='my_login')
def cart_update(request):
	pass



@login_required(login_url='my_login')
def checkout(request):
    user_cart = Cart.objects.get(user=request.user)
    cart_items = user_cart.items.all()

    if request.method == 'POST':
        form = CheckoutForm(request.POST)

        if form.is_valid():
            # Create a new order instance
            new_order = Order(
                user=request.user,
                address=form.cleaned_data['address'],
                phone_number=form.cleaned_data['phone_number'],
                payment_type=form.cleaned_data['payment_type'],
                total_price=user_cart.total_cart_price(),
            )
            new_order.save()

            # Associate cart items with the order
            new_order.items.set(cart_items)

            # Clear the cart after checkout
            user_cart.items.clear()

            return redirect('order_confirmation', order_id=new_order.id)
				
				

    else:
        form = CheckoutForm()

    context = {
        'form': form,
        'cart_items': cart_items,
    }

    return render(request, 'checkout.html', context)


@login_required(login_url='my_login')
def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id)

    context = {
        'order': order,
    }

    return render(request, 'order_confirmation.html', context)