from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from .models import Report
from .serializers import WeatherSerializer


class ReportMixinView(mixins.ListModelMixin):
    queryset = Report.objects.all()
    serializer_class = WeatherSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# class WeatherView(APIView):
#     def get(self, request, *args, **kwargs):
#         queryset = Report.objects.all()
#         serializer = WeatherSerializer(queryset, many = True)
#         return Response(serializer.data)
    


# Create your views here.
