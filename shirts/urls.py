from django.urls import path, include
from shirts import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

urlpatterns = [
    path('', views.home, name='home'),
    
    #Error handlers
    path('handler404/', views.handler404),
    path('handler500/', views.handler500),


    path('contact/', views.contact, name='contact'),
    path('orders/', views.orders, name='orders'),
    path('products/', views.products, name='products'),
    
    #Custom Admin
    path('admin_login/', views.admin_login, name='admin_login'),
    path('webadmin/', views.admin_dashboard, name='admin_dashboard'),
    path('all_users/', views.all_users, name='all_users'),
    path('all_products/', views.all_products, name='all_products'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_brand/', views.add_brand, name='add_brand'),
    path('add_occassion/', views.add_occassion, name='add_occassion'),
    path('add_color/', views.add_color, name='add_color'),
    path('add_neck/', views.add_neck, name='add_neck'),
    path('edit_product/<int:id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),
    
    
    #Cart
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart_detail'),    
    path('add_to_cart/<str:slug>/<str:size>', views.addtocart, name='add_to_cart'),
    # path('cart/<int:id>', views.remove_from_cart, name='remove_from_cart'),
    
    #product detail
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),

    #User Login/Signup 
    path('usersignup/', views.signup, name='signup'),
    path('userlogin/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('updateprofile/<str:user>', views.updateprofile, name='updateprofile'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    # path('profile/<str:username>', views.profile, name='profile'),
    path('profile/', views.profile, name='profile'),
    # path('process_payment/', views.process_payment, name='process_payment'),
    # path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-failed/', views.payment_failed, name='payment_failed'),
    path('payment-result/', views.payment_result, name='payment_result')



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
