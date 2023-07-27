from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from shell.shellapp import serializers
from shell.shellapp.models import Car


class SelectCars(APIView):
    def get(self, request):
        data = Car.objects.all()
        serializer = serializers.CarSerializer(data, context={"request": request}, many=True)
        return Response(serializer.data)
