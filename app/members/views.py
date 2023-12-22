from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render 
from rest_framework.views import APIView 
from .models import Member
from rest_framework.response import Response 
from .serializer import ReactSerializer

class ReactView(APIView): 
    serializer_class = ReactSerializer

    def get(self, request): 
        webinar_details = [
            {
                "Topic": webinar_detail.Topic,
                "Description": webinar_detail.Description,
                "By": webinar_detail.By,
                "Date": webinar_detail.Date,
                "Image": request.build_absolute_uri(webinar_detail.Image.url) if webinar_detail.Image else None
            }
            for webinar_detail in Member.objects.all()
        ] 
        return Response(webinar_details) 
  
    def post(self, request): 
        serializer = ReactSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return Response(serializer.data)
