from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import Http404
from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from .models import autorzy
from .serializers import biblioteka2
from .models import wypozyczenia
from .serializers import biblioteka3
from .models import kategorie
from .serializers import biblioteka4
from .models import wydawnictwo
from .serializers import biblioteka5
from .models import ksiazki
from .serializers import biblioteka6
from .models import czytelnicy
from .serializers import biblioteka7


class Autorzylista(APIView):

    def get(self, request):
        autorzyll = autorzy.objects.all()
        serializer = biblioteka2(autorzyll, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = biblioteka2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class wypozyczenial(APIView):

    def get(self, request):
        wypozyczeniall = wypozyczenia.objects.all()
        serializer = biblioteka3(wypozyczeniall, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = biblioteka3(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class kategoriel(APIView):

    def get(self, request):
        kategoriell = kategorie.objects.all()
        serializer = biblioteka4(kategoriell, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = biblioteka4(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class wydawnictwol(APIView):

    def get(self, request):
        wydawnictwoll = wydawnictwo.objects.all()
        serializer = biblioteka5(wydawnictwoll, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = biblioteka5(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ksiazkil(APIView):

    def get(self, request):
        ksiazkill = ksiazki.objects.all()
        serializer = biblioteka6(ksiazkill, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = biblioteka6(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class czytelnicyl(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        czytelnicyll = czytelnicy.objects.all()
        serializer = biblioteka7(czytelnicyll, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = biblioteka7(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

