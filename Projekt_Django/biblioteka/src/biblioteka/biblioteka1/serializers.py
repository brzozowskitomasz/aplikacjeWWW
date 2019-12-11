from rest_framework import serializers
from .models import autorzy
from .models import wypozyczenia
from .models import kategorie
from .models import wydawnictwo
from .models import ksiazki
from .models import czytelnicy

class biblioteka2(serializers.ModelSerializer):
    class Meta:
        model = autorzy
        fields = '__all__'


class biblioteka3(serializers.ModelSerializer):
    class Meta:
        model = wypozyczenia
        fields = '__all__'


class biblioteka4(serializers.ModelSerializer):
    class Meta:
        model = kategorie
        fields = '__all__'


class biblioteka5(serializers.ModelSerializer):
    class Meta:
        model = wydawnictwo
        fields = '__all__'


class biblioteka6(serializers.ModelSerializer):
    class Meta:
        model = ksiazki
        fields = '__all__'


class biblioteka7(serializers.ModelSerializer):
    class Meta:
        model = czytelnicy
        fields = '__all__'

