from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Vendor
from .forms import ProductForm

# Create your views here.
def become_vendor(request):
    return render(request, 'vendor/become_a_vendor.html')

def vendor_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            shop_name = request.POST['shop_name']
            shop_address = request.POST['shop_address']
            contact_number = request.POST['contact_number']
            shop_logo = request.FILES['shop_logo']
            shop_banner = request.FILES['shop_banner']
            fb_link = request.POST['fb_link']
            insta_link = request.POST['insta_link']
            linkedin_link = request.POST['linkedin_link']
            twitter_link = request.POST['twitter_link']

            vendor = Vendor.objects.create(name=user.username,shop_name=shop_name, shop_address=shop_address, contact_number=contact_number, facebook_link=fb_link, linkedin_link=linkedin_link, twitter_link=twitter_link, instagram_link=insta_link, shop_logo=shop_logo, shop_banner=shop_banner, created_by=user)

            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'vendor/vendor_registration.html', {'form':form})

@login_required
def vendor_admin(request):
    vendor = request.user.vendor
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.name)
            product.save()
            return redirect('vendor_admin')
    else:
        form = ProductForm()  

    context = {'vendor': vendor, 'form': form}
    return render(request, 'vendor/vendor_admin.html', context)




def all_vendors(request):
    all_vendors = Vendor.objects.all()
    return render(request, 'vendor/all_vendors.html', {'all_vendors':all_vendors})

