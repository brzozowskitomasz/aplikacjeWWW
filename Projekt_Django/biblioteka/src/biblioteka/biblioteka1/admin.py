from django.contrib import admin

from .models import wypozyczenia
from .models import kategorie
from .models import wydawnictwo
from .models import autorzy
from .models import ksiazki
from .models import czytelnicy

admin.site.register(wypozyczenia)
admin.site.register(kategorie)
admin.site.register(wydawnictwo)
admin.site.register(autorzy)
admin.site.register(ksiazki)
admin.site.register(czytelnicy)
# Register your models here.
