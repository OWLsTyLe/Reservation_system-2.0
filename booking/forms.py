from django import forms
from hotels.models import HotelRoom

class BookingForm(forms.Form):
    room = forms.ModelChoiceField(
        queryset=HotelRoom.objects.none(),  # спочатку пустий, буде оновлено у view
        required=True,
        label="Room",
        empty_label="Select a room"
    )
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Start Date"
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        label="End Date"
    )

    def __init__(self, *args, **kwargs):
        hotel = kwargs.pop('hotel', None)
        super().__init__(*args, **kwargs)
        if hotel:
            self.fields['room'].queryset = HotelRoom.objects.filter(hotel=hotel, available_count__gt=0)
