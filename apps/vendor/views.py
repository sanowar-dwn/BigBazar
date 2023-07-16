from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Vendor

# Create your views here.

def become_vendor(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            shop_name = request.POST['shop_name']
            shop_address = request.POST['shop_address']
            contact_number = request.POST['contact_number']
            shop_logo = request.POST['shop_logo']
            shop_banner = request.POST['shop_banner']
            fb_link = request.POST['fb_link']
            insta_link = request.POST['insta_link']
            linkedin_link = request.POST['linkedin_link']
            twitter_link = request.POST['twitter_link']

            vendor = Vendor.objects.create(name=user.username,shop_name=shop_name, shop_address=shop_address, contact_number=contact_number, facebook_link=fb_link, linkedin_link=linkedin_link, twitter_link=twitter_link, instagram_link=insta_link, shop_logo=shop_logo, shop_banner=shop_banner, created_by=user)

            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'vendor/become_vendor.html', {'form':form})