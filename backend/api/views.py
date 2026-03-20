from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType

from . import serializers as ContentSerializer
from content import models as ContentModel
# Create your views here.


class ExperienceView(generics.RetrieveAPIView): #returna a single object
    serializer_class = ContentSerializer.ExperienceSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"

    def get_queryset(self):
        return ContentModel.Experience.objects.filter(id=self.kwargs["id"])

class CategoryView(generics.ListAPIView): #returns a list of objects
    serializer_class = ContentSerializer.ExperienceSerializer # check this
    permission_classes = [AllowAny]


    # #get category name from input
    # category_name = self.k
    # #first search the category table and find the category id given that they gave the name
    # category_id = ContentModel.Category.objects.filter(name = self.kwargs["category"])
    # #then return all the experiences with that given category id

    def get_queryset(self):
        category_name = self.kwargs["category"]
        # category_id__name works even though Experience stores only category_id (Django does the join automatically).
        return ContentModel.Experience.objects.filter(category_id__name = category_name)



class LocationView(generics.ListAPIView):
    serializer_class = ContentSerializer.LocationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return ContentModel.Location.objects.all()