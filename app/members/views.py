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
        # Check if the 'Topic' field is present to determine the data type
        is_webinar_data = 'Topic' in request.data

        # Create a new serializer instance based on the data type
        serializer = ReactSerializer(data=request.data, many=is_webinar_data)

        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return Response(serializer.data)
