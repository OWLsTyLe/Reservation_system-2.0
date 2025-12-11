from django.core.mail import send_mail
import stripe
from django.http import JsonResponse
import json
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from hotels.models import Hotel, HotelRoom
from .forms import BookingForm


stripe.api_key = settings.STRIPE_SECRET_KEY

def send_booking_confirmation(user_email, booking):
    subject = "Підтвердження бронювання"
    message = f"""
    Вітаємо, {booking.user.username}!

    Ваше бронювання успішно створено.

    Готель: {booking.room.hotel.name}
    Тип номеру: {booking.room.room_type.name}
    Ціна за ніч: {booking.room.price_per_night} грн
    Дата заїзду: {booking.start_date}
    Дата виїзду: {booking.end_date}

    Дякуємо, що обрали наш сервіс!
    """
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user_email])

@login_required
def create_booking(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, hotel=hotel)
        if form.is_valid():
            room = form.cleaned_data['room']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # зменшення доступної кількості кімнат на 1
            if room.available_count > 0:
                room.available_count -= 1
                room.save()

                booking = Booking.objects.create(
                    user=request.user,
                    room=room,
                    start_date=start_date,
                    end_date=end_date
                )

                send_booking_confirmation(request.user.email, booking)
                return redirect('home')
            else:
                error = "Вибраний номер більше недоступний."
                return render(request, 'booking/create_booking.html', {'hotel': hotel, 'form': form, 'error': error})
    else:
        form = BookingForm(hotel=hotel)

    return render(request, 'booking/create_booking.html', {'hotel': hotel, 'form': form})




@login_required
def cancel_booking(request, booking_id):
    return redirect('home')

def account(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/acount.html', {
        'bookings': bookings,
        'stripe_public_key': settings.STRIPE_PUBLISHABLE_KEY,
    })

@login_required
def create_checkout_session(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid method'}, status=400)

    data = json.loads(request.body)
    booking_id = data.get('id')
    try:
        booking = Booking.objects.get(id=booking_id, user=request.user)
    except Booking.DoesNotExist:
        return JsonResponse({'error': 'Booking not found'}, status=404)

    amount = int(booking.total_price() * 100)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'uah',
                'product_data': {
                    'name': f'Бронювання {booking.room.hotel.name}',
                },
                'unit_amount': amount,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/success/?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='http://127.0.0.1:8000/cancel/',
        metadata={
            'booking_id': str(booking.id)
        }
    )

    return JsonResponse({'sessionId': session.id})

@login_required
def payment_success(request):
    session_id = request.GET.get('session_id')
    if session_id:
        try:
            session = stripe.checkout.Session.retrieve(session_id)
            booking_id = session.metadata.get('booking_id')
            if booking_id:
                booking = Booking.objects.get(id=booking_id, user=request.user)
                booking.is_paid = True
                booking.save()
        except Exception as e:
            print(f"Error in payment success handling: {e}")
    return render(request, 'main/index.html')

@login_required
def payment_cancel(request):
    return render(request, 'restourants/restourants.html')
