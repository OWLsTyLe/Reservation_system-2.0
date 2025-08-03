from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_booking, name='create_booking'),
    path('account/', views.account, name='account'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    # path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('<int:booking_id>/checkout/', views.create_checkout_session, name='booking_checkout'),
    path('success/', views.payment_success, name='payment_success'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
]