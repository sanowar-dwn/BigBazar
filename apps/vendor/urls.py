from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('become-a-vendor/', views.become_vendor, name='become_vendor'),
    path('vendor-registration/', views.vendor_registration, name='vendor_registration'),
    path('vendor-admin/', views.vendor_admin, name='vendor_admin'),
    path('all-vendors/', views.all_vendors, name='all_vendors'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='vendor/vendor_login.html'), name='login'),

]
