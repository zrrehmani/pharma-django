from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from Auth.models import Test
from .forms import ProductForm

@login_required(login_url='login')
class Home:
    def home(request):
        return render(request, 'Home/home.html')
    
    def product(request):
        test = Test.objects.all()
        return render(request, 'Home/product.html', {'test':test})
    
    def add_form(request):
        form = ProductForm()
        return render(request, 'Home/__product.html', {'form':form})
    
    # Start Add product 
    def add_product(request):
        if request.method == "POST":
            form = ProductForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                password = make_password(form.cleaned_data['password'])
                ins = Test.objects.create(name=name, email=email, password=password)
                if ins:
                    messages.success(request, 'Record has been saved successfull')
                else:
                    messages.error(request, 'Something went wrong, Please try again later')
                return redirect('product')
            else:
                form = ProductForm()
            return render(request, 'Home/__product.html', {'form':form})
    # End Add Product

    def edit_form(request, id):
        test = Test.objects.get(id=id)
        initial_values = {'name':test.name, 'email':test.email, 'password':test.password, 'pid':id}
        class EditForm(ProductForm):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.fields['password'].widget.input_type = 'hidden'
        form = EditForm(initial=initial_values)
        form.fields['pid'].label = ''
        form.fields['password'].label = ''
        return render(request, 'Home/__product.html', {'form':form})


    def edit_product(request):
        test = Test.objects.filter(id=request.POST.get('pid')).update(name=request.POST.get('name'), email=request.POST.get('email'))
        test = Test.objects.all()
        messages.success(request, 'Record has been updated successfully')
        return render(request, 'Home/product.html', {'test':test})
