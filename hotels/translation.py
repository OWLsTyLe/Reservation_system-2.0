from modeltranslation.translator import translator, TranslationOptions
from .models import Hotel, RoomType, HotelRoom

class HotelTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'address',)

translator.register(Hotel, HotelTranslationOptions)

class RoomTypeTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
translator.register(RoomType, RoomTypeTranslationOptions)

# class HotelRoomTranslationOptions(TranslationOptions):
#     fields = ('name', 'room_type',)
# translator.register(HotelRoom, HotelRoomTranslationOptions)