from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from booking.models import Booking


def index(request):
    return render(request, 'main/index.html')


def account(request):
    if not request.user.is_authenticated:
        return render(request, 'booking/need_login.html')

    bookings = (
        Booking.objects
        .filter(user=request.user)
        .select_related('room', 'room__hotel', 'room__room_type')
    )

    return render(request, 'booking/account.html', {
        'bookings': bookings
    })